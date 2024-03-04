import os
import unittest

from supabase import SupabaseClient, create_client
from supabase.client.exceptions import ConfigurationError


class TestDefaultClient(unittest.TestCase):
    def setUp(self) -> None:
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client = SupabaseClient(self.url, self.key)

    def test_invalid_create_client(self):
        for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
                try:
                    self.assertIsNone(create_client(url, key))
                except ConfigurationError:
                    self.assertTrue(1 == 1)
