from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class ClusterAPI:
    """API wrapper for cluster endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_cluster_info(self) -> Dict[str, Any]:
        """Get overall cluster information.
        Returns:
            dict: Cluster info.
        """
        path = "/configs/cluster/v1/cluster"
        return self.http.request("GET", path)

    def get_dscs(self) -> Dict[str, Any]:
        """List Distributed Services Cards (DSCs).
        Returns:
            dict: DSCs list.
        """
        path = "/configs/distributedservicecard/v1/distributedservicecards"
        return self.http.request("GET", path)

    def get_dsc_macs(self) -> Dict[str, Any]:
        """List DSC MAC addresses.
        Returns:
            dict: DSC MACs.
        """
        path = "/configs/distributedservicecard/v1/distributedservicecards/macs"
        return self.http.request("GET", path)

