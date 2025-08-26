from typing import Any, Dict, List, Optional
from pensando.core.http_client import HTTPClient

class ObjStoreAPI:
    """API wrapper for objstore endpoints."""
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_bucket(self, name: str) -> Dict[str, Any]:
        """Get an object store bucket.
        Args:
            name: Bucket name.
        Returns:
            dict: Bucket.
        """
        path = f"/configs/objstore/v1/tenant/{self.http.tenant}/buckets/{name}"
        return self.http.request("GET", path)

    def get_buckets(self) -> Dict[str, Any]:
        """List object store buckets.
        Returns:
            dict: Buckets.
        """
        path = f"/configs/objstore/v1/tenant/{self.http.tenant}/buckets"
        return self.http.request("GET", path)

