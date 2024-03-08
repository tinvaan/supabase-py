
from postgrest import APIError as PostgrestAPIError
from postgrest import APIResponse as PostgrestAPIResponse
from storage3.utils import StorageException

from ..__version__ import __version__
from ..lib.realtime_client import SupabaseRealtimeClient

from ..lib.client_options import ClientOptions
from .default import APIClient, AsyncAPI
from .default import SyncStorageClient as SupabaseStorageClient


class SupabaseClient:
    @classmethod
    def create(cls, url, key, options=ClientOptions()):
        if options.is_async:
            return AsyncAPI.create(url, key, options)
        return APIClient.create(url, key, options)


def create_client(
    supabase_url: str,
    supabase_key: str,
    options: ClientOptions = ClientOptions(),
) -> SupabaseClient:
    """Create client function to instantiate supabase client like JS runtime.

    Parameters
    ----------
    supabase_url: str
        The URL to the Supabase instance that should be connected to.
    supabase_key: str
        The API key to the Supabase instance that should be connected to.
    **options
        Any extra settings to be optionally specified - also see the
        `DEFAULT_OPTIONS` dict.

    Examples
    --------
    Instantiating the client.
    >>> import os
    >>> from supabase import create_client, Client
    >>>
    >>> url: str = os.environ.get("SUPABASE_TEST_URL")
    >>> key: str = os.environ.get("SUPABASE_TEST_KEY")
    >>> supabase: Client = create_client(url, key)

    Returns
    -------
    Client
    """
    return SupabaseClient.create(supabase_url, supabase_key, options)


__all__ = [
    "__version__",
    "create_client",
    "ClientOptions",
    "PostgrestAPIError",
    "PostgrestAPIResponse",
    "StorageException",
    "SupabaseClient",
    "SupabaseRealtimeClient",
    "SupabaseStorageClient",
]
