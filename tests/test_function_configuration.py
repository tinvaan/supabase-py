import unittest

from supabase import SupabaseClient


class TestFunctionsClient(unittest.TestCase):
    def setUp(self) -> None:
        self.ref = "ooqqmozurnggtljmjkii"
        self.url = f"https://{self.ref}.supabase.co"
        self.key = "xxxxxxxxxxxxxx.xxxxxxxxxxxxxxx.xxxxxxxxxxxxxxx"
        self.client = SupabaseClient(self.url, self.key)

    def test_functions_client_initialization(self):
        assert (
            self.client.functions_url == f"https://{self.ref}.supabase.co/functions/v1"
        )

        url = "https://localhost:54322"
        client = SupabaseClient(url, self.key)
        assert client.functions_url == f"{url}/functions/v1"
