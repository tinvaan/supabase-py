import os
import unittest

from postgrest.exceptions import APIError

from supabase import SupabaseClient, create_client
from supabase.client.exceptions import ConfigurationError

from . import AsyncTestClient, TestClient


def test_create_client():
    for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
        for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            try:
                assert create_client(url, key)
            except ConfigurationError:
                assert True
    assert create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


class TestSync(TestClient):
    def test_create(self):
        for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
                with self.assertRaises(ConfigurationError):
                    SupabaseClient.create(url, key)
        self.assertIsNotNone(SupabaseClient.create(self.url, self.key))

    def test_table_delete(self):
        with self.assertRaises(APIError):
            self.client.table("foobar").delete().eq("id", 1).execute()

        op = self.client.table(self.table).delete().eq("name", "Canada").execute()
        self.assertIsNotNone(op)
        for d in op.data:
            self.assertEqual(d.get("name"), "Canada")

    def test_table_insert(self):
        with self.assertRaises(APIError):
            self.client.table("foobar").insert({"name": "barfoo"}).execute()

        self.countries.add("Wadiya")
        op = self.client.table(self.table).insert({"name": "Wadiya"}).execute()
        self.assertIsNotNone(op)
        for d in op.data:
            self.assertEqual(d.get("name"), "Wadiya")

    def test_table_select(self):
        with self.assertRaises(APIError):
            self.client.table("foobar").select().eq("id", 1).execute()

        op = self.client.table(self.table).select("*").execute()
        self.assertIsNotNone(op)
        self.assertEqual(len(op.data), len(self.countries))

        op = self.client.table(self.table).select("*").eq("name", "Canada").execute()
        self.assertIsNotNone(op)
        self.assertEqual(len(op.data), 1)

    def test_table_update(self):
        with self.assertRaises(APIError):
            self.client.table("foobar").update({"foo": "bar"}).execute()
            self.client.table(self.table).update({"foo": "bar"}).eq("name", "Canada").execute()
            self.client.table(self.table).update({"name": "Australia"}).eq("foo", "bar").execute()

        self.countries.add("Denmark")
        op = self.client.table(self.table).update({"name": "Denmark"}).eq("name", "Dubai").execute()
        self.assertIsNotNone(op)
        for d in op.data:
            self.assertEqual(d.get("name"), "Denmark")

    def test_rpc(self):
        with self.assertRaises(APIError):
            self.client.rpc("dead", {"foo": "bar"}).execute()

        op = self.client.rpc("alive", {}).execute()
        self.assertTrue(op.data)

    @unittest.skip("TODO")
    def test_listen_to_auth_events(self):
        pass


class TestAsync(AsyncTestClient):
    async def test_create(self):
        for url in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
            for key in ("", None, "valeefgpoqwjgpj", 139, -1, {}, []):
                with self.assertRaises(ConfigurationError):
                    await SupabaseClient.create(url, key, options=self.opts)
        self.assertIsNotNone(await SupabaseClient.create(self.url, self.key, options=self.opts))

    async def test_table_delete(self):
        with self.assertRaises(APIError):
            await self.client.table("foobar").delete().eq("id", 1).execute()

        op = await self.client.table(self.table).delete().eq("name", "Canada").execute()
        self.assertIsNotNone(op)
        for d in op.data:
            self.assertEqual(d.get("name"), "Canada")

    async def test_table_insert(self):
        with self.assertRaises(APIError):
            await self.client.table("foobar").insert({"name": "barfoo"}).execute()

        self.countries.add("Wadiya")
        op = await self.client.table(self.table).insert({"name": "Wadiya"}).execute()
        self.assertIsNotNone(op)
        for d in op.data:
            self.assertEqual(d.get("name"), "Wadiya")

    async def test_table_select(self):
        with self.assertRaises(APIError):
            await self.client.table("foobar").select().eq("id", 1).execute()

        op = await self.client.table(self.table).select("*").execute()
        self.assertIsNotNone(op)
        self.assertEqual(len(op.data), len(self.countries))

        op = await self.client.table(self.table).select("*").eq("name", "Canada").execute()
        self.assertIsNotNone(op)
        self.assertEqual(len(op.data), 1)

    async def test_table_update(self):
        with self.assertRaises(APIError):
            await self.client.table("foobar").update({"foo": "bar"}).execute()
            await self.client.table(self.table).update({"foo": "bar"}).eq("name", "Canada").execute()
            await self.client.table(self.table).update({"name": "Australia"}).eq("foo", "bar").execute()

        self.countries.add("Denmark")
        op = await self.client.table(self.table).update({"name": "Denmark"}).eq("name", "Dubai").execute()
        self.assertIsNotNone(op)
        for d in op.data:
            self.assertEqual(d.get("name"), "Denmark")

    async def test_rpc(self):
        with self.assertRaises(APIError):
            await self.client.rpc("dead", {"foo": "bar"}).execute()

        op = await self.client.rpc("alive", {}).execute()
        self.assertTrue(op.data)
