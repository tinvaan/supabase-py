import os
import unittest

from supabase import SupabaseClient, create_client
from supabase.client.exceptions import ConfigurationError
from supabase.lib.client_options import ClientOptions


def test_create_client():
    for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
        for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            try:
                assert create_client(url, key)
            except ConfigurationError:
                assert True

    assert create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


class TestSync(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = os.getenv("SUPABASE_URL")
        cls.key = os.getenv("SUPABASE_KEY")
        cls.schema = os.getenv("SUPABASE_TEST_SCHEMA", "unittest")

    def setUp(self):
        self.opts = ClientOptions(schema=self.schema)
        self.client = SupabaseClient.create(self.url, self.key, options=self.opts)

    def test_create(self):
        for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
                with self.assertRaises(ConfigurationError):
                    SupabaseClient.create(url, key)

        self.assertIsNotNone(SupabaseClient.create(self.url, self.key))

    @unittest.skip('TODO: Find the correct usage')
    def test_from_(self):
        op = self.client.from_("countries").insert({"name": "Wadiya"}).execute()
        self.assertIsNotNone(op)

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
