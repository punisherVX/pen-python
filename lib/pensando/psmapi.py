import pathlib
import configparser
import logging
import os
from typing import Optional

from pensando.core.http_client import HTTPClient
from pensando.modules.auth import AuthAPI
from pensando.modules.cluster import ClusterAPI
from pensando.modules.events import EventsAPI
from pensando.modules.monitoring import MonitoringAPI
from pensando.modules.objstore import ObjStoreAPI
from pensando.modules.security import SecurityAPI
from pensando.modules.sysruntime import SysRuntimeAPI
from pensando.modules.telemetry import TelemetryAPI
from pensando.modules.workloads import WorkloadsAPI


class PenConfig:
    """Parses configuration files for PSM connection settings.

    The expected INI section is ``[PSM_API]`` with keys: ``server``, ``user``, ``password``, ``tenant``.
    """

    def __init__(self, section: str, config_file: str):
        self.config_file = pathlib.Path(config_file)
        self.section = section
        self.conf_dict = {}

        if self.config_file.is_file():
            self.conf_dict = self._parse_config()
        else:
            logging.warning(f"Config file {config_file} not found. Using defaults.")

    def _parse_config(self):
        cfg_dict = {}
        config = configparser.RawConfigParser()
        config.read(str(self.config_file))
        cfg_dict = dict(config.items(self.section))
        logging.debug(f"Parameters set for {self.section}: {cfg_dict}")
        return cfg_dict

    def get(self, item: str, default: Optional[str] = None) -> Optional[str]:
        return self.conf_dict.get(item, default)


class PSM:
    """Main API client that exposes all endpoint groups via composition.

    Examples:
        >>> psm = PSM(server="https://psm", user="admin", password="***", tenant="default")
        >>> psm.auth.get_users()
    """

    def __init__(self, server: Optional[str] = None, user: Optional[str] = None,
                 password: Optional[str] = None, tenant: Optional[str] = None,
                 config: Optional[str] = None, verify_ssl: bool = False):
        if not server:
            # Try environment variables first
            server = os.getenv("PSM_SERVER")
            user = os.getenv("PSM_USER")
            password = os.getenv("PSM_PASSWORD")
            tenant = os.getenv("PSM_TENANT")

            if not all([server, user, password, tenant]):
                if not config:
                    config = f"{str(pathlib.Path.home())}/.penrc"
                cfg = PenConfig("PSM_API", config)
                server = server or cfg.get("server")
                user = user or cfg.get("user")
                password = password or cfg.get("password")
                tenant = tenant or cfg.get("tenant")

        if not all([server, user, password, tenant]):
            raise ValueError("server, user, password, and tenant are required")

        self.http = HTTPClient(server, user, password, tenant, verify_ssl=verify_ssl)

        # Attach API modules
        self.auth = AuthAPI(self.http)
        self.cluster = ClusterAPI(self.http)
        self.events = EventsAPI(self.http)
        self.monitoring = MonitoringAPI(self.http)
        self.objstore = ObjStoreAPI(self.http)
        self.security = SecurityAPI(self.http)
        self.sysruntime = SysRuntimeAPI(self.http)
        self.telemetry = TelemetryAPI(self.http)
        self.workloads = WorkloadsAPI(self.http)
