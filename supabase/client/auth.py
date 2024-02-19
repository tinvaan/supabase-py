
from gotrue import AsyncGoTrueClient, AsyncMemoryStorage
from gotrue import SyncGoTrueClient, SyncMemoryStorage


class Auth:
    @classmethod
    def create(cls, *, url, headers, storage_key, auto_refresh_token, persist_session,
                 storage=AsyncMemoryStorage(), http_client: None, flow_type='implicit', **kwargs):
        args = {
            'url': url,
            'headers': headers or {},
            'storage_key': storage_key,
            'auto_refresh_token': auto_refresh_token,
            'persist_session': persist_session,
            'storage': storage,
            'http_client': http_client,
            'flow_type': flow_type
        }
        if bool(kwargs.get('async', False)):
            # Ensure async memory storage
            args.update({'storage': AsyncMemoryStorage()})
            return AsyncGoTrueClient(**args)

        # Ensure sync memory storage
        args.update({'storage': SyncMemoryStorage()})
        return SyncGoTrueClient(**args)
