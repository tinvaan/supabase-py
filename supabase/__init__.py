from postgrest import APIError as PostgrestAPIError
from postgrest import APIResponse as PostgrestAPIResponse
from storage3.utils import StorageException

from .__version__ import __version__
from .client.auth import AuthClient
from .client.default import SupabaseClient, create_client
from .lib.realtime_client import SupabaseRealtimeClient

__all__ = [
    "create_client",
    "Client",
    "SupabaseAuthClient",
    "SupabaseStorageClient",
    "SupabaseRealtimeClient",
    "PostgrestAPIError",
    "PostgrestAPIResponse",
    "StorageException",
    "__version__",
]
