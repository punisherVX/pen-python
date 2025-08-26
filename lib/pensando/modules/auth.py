from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class AuthAPI:
    """API wrapper for auth endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_authentication_policy(self) -> Dict[str, Any]:
        """Get the cluster authentication policy.
        Returns:
            dict: Authentication policy.
        """
        path = "/configs/auth/v1/authn-policy"
        return self.http.request("GET", path)

    def get_role_bindings(self) -> Dict[str, Any]:
        """List role bindings for the current tenant.
        Returns:
            dict: Role bindings.
        """
        path = f"/configs/auth/v1/tenant/{self.http.tenant}/role-bindings"
        return self.http.request("GET", path)

    def get_user(self, user: str) -> Dict[str, Any]:
        """Get a single user.
        Args:
            user: Username.
        Returns:
            dict: User details.
        """
        path = f"/configs/auth/v1/tenant/{self.http.tenant}/users/{user}"
        return self.http.request("GET", path)

    def get_users(self) -> Dict[str, Any]:
        """List all users in the tenant.
        Returns:
            dict: Users.
        """
        path = f"/configs/auth/v1/tenant/{self.http.tenant}/users"
        return self.http.request("GET", path)

    def get_user_prefs(self, user: str) -> Dict[str, Any]:
        """Get preferences for a user.
        Args:
            user: Username.
        Returns:
            dict: User preferences.
        """
        path = f"/configs/auth/v1/tenant/{self.http.tenant}/user-preferences/{user}"
        return self.http.request("GET", path)

