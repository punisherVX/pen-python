from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class TelemetryAPI:
    """API wrapper for telemetry endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_metrics(self, namespace: str, kind: str, field: str, tenant: Optional[str] = None) -> Dict[str, Any]:
        """Fetch metrics for a given resource.
        Args:
            namespace: Namespace of the resource.
            kind: Resource kind.
            field: Field to fetch.
            tenant: Optional tenant override.
        Returns:
            dict: Metrics response.
        """
        t = tenant or self.http.tenant
        path = f"/telemetry/v1/tenant/{t}/metrics?namespace={namespace}&kind={kind}&field={field}"
        return self.http.request("GET", path)

