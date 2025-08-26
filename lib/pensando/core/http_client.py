import logging
from typing import Any, Dict, Optional
import requests
from requests import Response, Session
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, Timeout, ConnectionError
from urllib3.util.retry import Retry


class APIError(Exception):
    """Custom exception for API errors."""
    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[Response] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class HTTPClient:
    """Centralized HTTP client for PSM REST API communication.
    
    Args:
        server: Base URL of the PSM (e.g., https://psm.example.com).
        user: Username.
        password: Password.
        tenant: Tenant name.
        verify_ssl: Whether to verify TLS certificates.
    """
    DEFAULT_TIMEOUT = 30

    def __init__(self, server: str, user: str, password: str, tenant: str, verify_ssl: bool = False, timeout: int = DEFAULT_TIMEOUT):
        self.server = server.rstrip("/")
        self.user = user
        self.password = password
        self.tenant = tenant
        self.session: Session = requests.Session()
        self.session.verify = verify_ssl
        self.DEFAULT_TIMEOUT = timeout

        # Retries with backoff for idempotent requests
        retry = Retry(total=3, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504), allowed_methods=("GET", "PUT", "DELETE", "OPTIONS", "HEAD"))
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Default headers
        self.session.headers.update({"Accept": "application/json"})

        self._login()

    def _login(self) -> Dict[str, Any]:
        """Authenticate and persist the session cookie/token.
        
        Returns:
            dict: JSON response from login endpoint.
        
        Raises:
            APIError: If authentication fails.
        """
        url = f"{self.server}/v1/login"
        data = {"username": self.user, "password": self.password, "tenant": self.tenant}
        resp = self.session.post(url, json=data, timeout=self.DEFAULT_TIMEOUT)
        if not resp.ok:
            raise APIError(f"Login failed: {resp.text}", resp.status_code, resp)
        logging.debug("Login successful")
        return resp.json()

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None,
                json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
                timeout: Optional[int] = None) -> Dict[str, Any]:
        """Generic request method used by all API calls.
        
        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE).
            path: Path appended to the base server URL (must start with '/').
            params: Query parameters.
            json: JSON body to send.
            headers: Optional request headers.
            timeout: Optional per-request timeout in seconds.
        
        Returns:
            dict: Parsed JSON response.
        
        Raises:
            APIError: For network errors or non-2xx responses.
        """
        if not path.startswith('/'):
            raise ValueError("path must start with '/'")
        url = f"{self.server}{path}"
        timeout = timeout or self.DEFAULT_TIMEOUT

        try:
            resp = self.session.request(method, url, params=params, json=json,
                                        headers=headers, timeout=timeout)
            if not resp.ok:
                raise APIError(f"HTTP {resp.status_code} error for {url}: {resp.text}",
                               resp.status_code, resp)
            # Some endpoints may return empty body; guard for that
            if resp.content and resp.headers.get("Content-Type", "").startswith("application/json"):
                return resp.json()
            return {}
        except (Timeout, ConnectionError) as e:
            logging.error(f"Network error: {e}")
            raise APIError(f"Network error: {e}")
        except RequestException as e:
            logging.error(f"Unexpected request error: {e}")
            raise APIError(f"Unexpected request error: {e}")
