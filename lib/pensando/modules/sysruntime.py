from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class SysRuntimeAPI:
    """API wrapper for sysruntime endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_system_info(self) -> Dict[str, Any]:
        """Get system runtime information.
        Returns:
            dict: System info.
        """
        path = "/sysruntime/v1/sysinfo"
        return self.http.request("GET", path)

