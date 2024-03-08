from postgrest import APIError as PostgrestAPIError
from postgrest import APIResponse as PostgrestAPIResponse
from storage3.utils import StorageException

from .__version__ import __version__
from .client import create_client, SupabaseClient
from .client.services import Auth as SupabaseAuthClient
from .client.services import Storage as SupabaseStorageClient
from .lib import SupabaseRealtimeClient



__all__ = [
    "create_client",
    "Client",
    "SupabaseClient",
    "SupabaseAuthClient",
    "SupabaseStorageClient",
    "SupabaseRealtimeClient",
    "PostgrestAPIError",
    "PostgrestAPIResponse",
    "StorageException",
    "__version__",
]
