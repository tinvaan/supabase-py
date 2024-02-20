
import os
import unittest

from supabase import SupabaseClient
from supabase.client.exceptions import ConfigurationError
from supabase.lib.client_options import ClientOptions

class TestSync(unittest.TestCase):
    def setUp(self) -> None:
        self.client = SupabaseClient.create(os.environ.get('SUPABASE_URL'),
                                            os.environ.get('SUPABASE_KEY'))

    def test_create(self):
        with self.assertRaises(ConfigurationError):
            SupabaseClient.create(None, None)
            SupabaseClient.create(123, "foobar")
            SupabaseClient.create(None, os.environ.get('SUPABASE_KEY'))
            SupabaseClient.create(os.environ.get('URL', False), os.environ.get('KEY', True))

        self.assertIsNotNone(SupabaseClient.create(os.environ.get('SUPABASE_URL'),
                                                   os.environ.get('SUPABASE_KEY')))

    def test_from_(self):
        """
        user=postgres.naovdfdeqttfibikfgzk password=[YOUR-PASSWORD] host=aws-0-ap-south-1.pooler.supabase.com port=5432 dbname=postgres
        """
        pass

    def test_rpc(self):
        pass

    def test_get_token_header(self):
        pass

    def test_listen_to_auth_events(self):
        pass

    def tearDown(self) -> None:
        pass


class TestAsync(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_create(self):
        pass

    def test_get_token_header(self):
        pass

    def tearDown(self) -> None:
        pass
