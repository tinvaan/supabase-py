from postgrest import APIError as PostgrestAPIError
from postgrest import APIResponse as PostgrestAPIResponse
from storage3.utils import StorageException

from ..__version__ import __version__
from ..lib.realtime_client import SupabaseRealtimeClient
from .auth import AuthClient
from .default import ClientOptions, SupabaseClient
from .default import SyncStorageClient as SupabaseStorageClient
from .default import create_client

__all__ = [
    "__version__",
    "create_client",
    "AuthClient",
    "ClientOptions",
    "PostgrestAPIError",
    "PostgrestAPIResponse",
    "StorageException",
    "SupabaseClient",
    "SupabaseRealtimeClient",
    "SupabaseStorageClient",
]
