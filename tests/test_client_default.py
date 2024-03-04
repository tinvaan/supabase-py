import os
import unittest

from postgrest.exceptions import APIError
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
        cls.rows = []
        cls.table = "countries"
        cls.url = os.getenv("SUPABASE_URL")
        cls.key = os.getenv("SUPABASE_KEY")
        cls.schema = os.getenv("SUPABASE_TEST_SCHEMA", "public")

    def setUp(self):
        self.opts = ClientOptions(schema=self.schema)
        self.client = SupabaseClient.create(self.url, self.key, options=self.opts)
        assert len(self.rows) == 0, "Test table state is not pristine"

    def test_create(self):
        for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
                with self.assertRaises(ConfigurationError):
                    SupabaseClient.create(url, key)

        self.assertIsNotNone(SupabaseClient.create(self.url, self.key))

    def test_table(self):
        op = self.client.table(self.table).insert({"name": "Wadiya"}).execute()
        self.rows.extend(op.data)

        self.assertIsNotNone(op)
        self.assertGreaterEqual(len(op.data), 1)

    def test_rpc(self):
        with self.assertRaises(APIError):
            self.client.rpc("dead", {"foo": "bar"}).execute()

        op = self.client.rpc("alive", {}).execute()
        self.assertTrue(op.data)

    @unittest.skip("TODO")
    def test_listen_to_auth_events(self):
        pass

    def tearDown(self) -> None:
        for row in self.rows:
            self.client.table(self.table).delete().eq("id", row.get('id')).execute()
        self.rows.clear()


class TestAsync(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_create(self):
        pass

    def test_get_token_header(self):
        pass

    def tearDown(self) -> None:
        pass
