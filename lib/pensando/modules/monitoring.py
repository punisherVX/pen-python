from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class MonitoringAPI:
    """API wrapper for monitoring endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_alerts(self) -> Dict[str, Any]:
        """List alerts for the tenant.
        Returns:
            dict: Alerts.
        """
        path = f"/monitoring/v1/tenant/{self.http.tenant}/alerts"
        return self.http.request("GET", path)

    def get_alert_object(self, uuid: str) -> Dict[str, Any]:
        """Get a specific alert by UUID.
        Args:
            uuid: Alert UUID.
        Returns:
            dict: Alert object.
        """
        path = f"/monitoring/v1/tenant/{self.http.tenant}/alerts/{uuid}"
        return self.http.request("GET", path)

    def get_app(self, name: str) -> Dict[str, Any]:
        """Get an application definition.
        Args:
            name: App name.
        Returns:
            dict: App object.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/apps/{name}"
        return self.http.request("GET", path)

    def get_endpoint(self, name: str) -> Dict[str, Any]:
        """Get an endpoint by name.
        Args:
            name: Endpoint name.
        Returns:
            dict: Endpoint object.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/endpoints/{name}"
        return self.http.request("GET", path)

    def get_endpoints(self) -> Dict[str, Any]:
        """List all endpoints.
        Returns:
            dict: Endpoints.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/endpoints"
        return self.http.request("GET", path)

    def get_ip_endpoints(self) -> Dict[str, Any]:
        """List all IP endpoints.
        Returns:
            dict: IP endpoints.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/ipendpoints"
        return self.http.request("GET", path)

    def get_security_policies(self) -> Dict[str, Any]:
        """List security policies for the tenant.
        Returns:
            dict: Policies.
        """
        path = f"/configs/security/v1/tenant/{self.http.tenant}/networksecuritypolicies"
        return self.http.request("GET", path)

    def get_flow_exports(self) -> Dict[str, Any]:
        """List flow export policies.
        Returns:
            dict: Flow export policies.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/flowexportpolicies"
        return self.http.request("GET", path)

    def get_collector(self, name: str) -> Dict[str, Any]:
        """Get a collector by name.
        Args:
            name: Collector name.
        Returns:
            dict: Collector.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/collectors/{name}"
        return self.http.request("GET", path)

    def get_collectors(self) -> Dict[str, Any]:
        """List collectors.
        Returns:
            dict: Collectors.
        """
        path = f"/configs/monitoring/v1/tenant/{self.http.tenant}/collectors"
        return self.http.request("GET", path)

