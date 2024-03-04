import os
import unittest

from supabase import SupabaseClient
from supabase.lib.client_options import ClientOptions


class ClientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = "countries"
        cls.url = os.getenv("SUPABASE_URL")
        cls.key = os.getenv("SUPABASE_KEY")
        cls.schema = os.getenv("SUPABASE_TEST_SCHEMA", "public")
        cls.countries = ["Argentina", "Brazil", "Canada", "Dubai"]

    def setUp(self):
        self.opts = ClientOptions(schema=self.schema)
        self.client = SupabaseClient.create(self.url, self.key, options=self.opts)
        for country in self.countries:
            self.client.table(self.table).insert({"name": country}).execute()

    def tearDown(self):
        for country in self.countries:
            self.client.table(self.table).delete().eq("name", country).execute()
        self.countries.clear()
