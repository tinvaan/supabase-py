import os

from unittest import IsolatedAsyncioTestCase, TestCase
from gotrue import AsyncMemoryStorage

from supabase import SupabaseClient
from supabase.lib.client_options import ClientOptions


class TestClient(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = "countries"
        cls.url = os.getenv("SUPABASE_URL")
        cls.key = os.getenv("SUPABASE_KEY")
        cls.schema = os.getenv("SUPABASE_TEST_SCHEMA", "public")
        cls.countries = set(["Argentina", "Brazil", "Canada", "Dubai"])

    def setUp(self):
        self.opts = ClientOptions(schema=self.schema)
        self.client = SupabaseClient.create(self.url, self.key, options=self.opts)
        for country in self.countries:
            self.client.table(self.table).insert({"name": country}).execute()

    def tearDown(self):
        for country in self.countries:
            self.client.table(self.table).delete().eq("name", country).execute()


class AsyncTestClient(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = "countries"
        cls.url = os.getenv("SUPABASE_URL")
        cls.key = os.getenv("SUPABASE_KEY")
        cls.schema = os.getenv("SUPABASE_TEST_SCHEMA", "public")
        cls.countries = set(["Argentina", "Brazil", "Canada", "Dubai"])

    async def asyncSetUp(self):
        self.opts = ClientOptions(schema=self.schema, is_async=True, storage=AsyncMemoryStorage())
        self.client = await SupabaseClient.create(self.url, self.key, options=self.opts)
        for country in self.countries:
            await self.client.table(self.table).insert({"name": country}).execute()

    async def asyncTearDown(self):
        for country in self.countries:
            await self.client.table(self.table).delete().eq("name", country).execute()
