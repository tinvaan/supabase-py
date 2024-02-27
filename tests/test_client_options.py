import unittest

from gotrue import SyncMemoryStorage

from supabase.lib.client_options import ClientOptions


class TestClientOptions(unittest.TestCase):
    def setUp(self) -> None:
        self.storage = SyncMemoryStorage()
        self.storage.set_item("key", "value")
        self.options = ClientOptions(
            schema="schema",
            headers={"key": "value"},
            auto_refresh_token=False,
            persist_session=False,
            storage=self.storage,
            realtime={"key": "value"},
        )

    def test_replace_returns_updated_options(self) -> None:
        self.assertEqual(
            self.options.replace(schema="new schema"),
            ClientOptions(
                schema="new schema",
                headers={"key": "value"},
                auto_refresh_token=False,
                persist_session=False,
                storage=self.storage,
                realtime={"key": "value"},
            ),
        )

    def test_replace_updates_only_new_options(self):
        modified = self.options.replace()
        modified.storage.set_item("key", "new_value")
        self.assertEqual(modified.storage.get_item("key"), "new_value")
        self.assertEqual(self.options.storage.get_item("key"), "new_value")
