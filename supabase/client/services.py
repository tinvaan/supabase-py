
from typing import Union

from gotrue import AsyncMemoryStorage, AsyncGoTrueClient, SyncMemoryStorage, SyncGoTrueClient
from postgrest import AsyncPostgrestClient, SyncPostgrestClient
from storage3 import SyncStorageClient, AsyncStorageClient
from supafunc import AsyncFunctionsClient, SyncFunctionsClient


class Auth:
    @classmethod
    def create(cls, *, url, headers=None, storage_key=None, auto_refresh_token=None,
                       persist_session=True, storage=None, http_client=None, flow_type='implicit',
                       **kwargs) -> Union[SyncGoTrueClient, AsyncGoTrueClient]:
        args = {
            "url": url,
            "headers": headers or {},
            "storage_key": storage_key,
            "auto_refresh_token": auto_refresh_token,
            "persist_session": persist_session,
            "storage": storage,
            "http_client": http_client,
            "flow_type": flow_type,
        }
        if bool(kwargs.get('is_async', False)):
            # Ensure async memory storage
            args.update({'storage': AsyncMemoryStorage()})
            return AsyncGoTrueClient(**args)

        # Ensure sync memory storage
        args.update({'storage': SyncMemoryStorage()})
        return SyncGoTrueClient(**args)


class Functions:
    @classmethod
    def create(cls, url, headers, **kwargs) -> Union[SyncFunctionsClient, AsyncFunctionsClient]:
        if bool(kwargs.get('is_async', False)):
            return AsyncFunctionsClient(url, headers)
        return SyncFunctionsClient(url, headers)


class PgREST:
    @classmethod
    def create(
        cls, url, headers=None, schema=None, timeout=None, **kwargs
    ) -> Union[SyncPostgrestClient, AsyncPostgrestClient]:
        if bool(kwargs.get('is_async', False)):
            return AsyncPostgrestClient(url, headers=headers, schema=schema, timeout=timeout)
        return SyncPostgrestClient(url, headers=headers, schema=schema, timeout=timeout)


class Storage:
    @classmethod
    def create(cls, url, headers=None, timeout=None, **kwargs) -> Union[SyncStorageClient, AsyncStorageClient]:
        if bool(kwargs.get('is_async', False)):
            return AsyncStorageClient(url, headers, timeout)
        return SyncStorageClient(url, headers, timeout)
