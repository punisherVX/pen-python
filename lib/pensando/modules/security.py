from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class SecurityAPI:
    """API wrapper for security endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_network_security_policy(self, name: str) -> Dict[str, Any]:
        """Get a network security policy.
        Args:
            name: Policy name.
        Returns:
            dict: Policy object.
        """
        path = f"/configs/security/v1/tenant/{self.http.tenant}/networksecuritypolicies/{name}"
        return self.http.request("GET", path)

    def get_network_security_policies(self) -> Dict[str, Any]:
        """List network security policies.
        Returns:
            dict: Policies.
        """
        path = f"/configs/security/v1/tenant/{self.http.tenant}/networksecuritypolicies"
        return self.http.request("GET", path)

