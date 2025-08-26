from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class EventsAPI:
    """API wrapper for events endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_events(self, kind: str, namespace: Optional[str] = None) -> Dict[str, Any]:
        """Query events.
        Args:
            kind: Object kind to filter.
            namespace: Optional namespace/tenant.
        Returns:
            dict: Events.
        """
        ns = namespace or self.http.tenant
        path = f"/events/v1/tenant/{ns}/events?kind={kind}"
        return self.http.request("GET", path)

