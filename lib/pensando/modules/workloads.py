from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class WorkloadsAPI:
    """API wrapper for workloads endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_workloads(self) -> Dict[str, Any]:
        """List workloads.
        Returns:
            dict: Workloads.
        """
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads"
        return self.http.request("GET", path)

    def get_workload(self, name: str) -> Dict[str, Any]:
        """Get a specific workload by name.
        Args:
            name: Workload name.
        Returns:
            dict: Workload.
        """
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads/{name}"
        return self.http.request("GET", path)

    def del_workload(self, name: str) -> Dict[str, Any]:
        """Delete a workload by name.
        Args:
            name: Workload name.
        Returns:
            dict: Delete response.
        """
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads/{name}"
        return self.http.request("DELETE", path)

    def add_workload_label(self, name: str, key: str, value: str) -> Dict[str, Any]:
        """Add or update a label on a workload.
        Args:
            name: Workload name.
            key: Label key.
            value: Label value.
        Returns:
            dict: Update response.
        """
        body = {"meta": {"name": name, "tenant": self.http.tenant}, "labels": {key: value}}
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads/{name}"
        return self.http.request("PUT", path, json=body)

    def update_workload_labels(self, name: str, labels: Dict[str, str]) -> Dict[str, Any]:
        """Replace labels on a workload.
        Args:
            name: Workload name.
            labels: Mapping of label key/value.
        Returns:
            dict: Update response.
        """
        body = {"meta": {"name": name, "tenant": self.http.tenant}, "labels": labels}
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads/{name}"
        return self.http.request("PUT", path, json=body)

    def get_workload_labels(self, name: str) -> Dict[str, Any]:
        """Get labels for a workload.
        Args:
            name: Workload name.
        Returns:
            dict: Labels object.
        """
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads/{name}"
        return self.http.request("GET", path)

    def del_workload_label(self, name: str, key: str) -> Dict[str, Any]:
        """Delete a label from a workload.
        Args:
            name: Workload name.
            key: Label key to remove.
        Returns:
            dict: Update response.
        """
        # Assuming PATCH semantics supported; fallback could be PUT with modified body.
        body = {"meta": {"name": name, "tenant": self.http.tenant}, "labels": {key: None}}
        path = f"/configs/workload/v1/tenant/{self.http.tenant}/workloads/{name}"
        return self.http.request("PATCH", path, json=body)

