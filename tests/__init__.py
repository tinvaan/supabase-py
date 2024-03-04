
import os
import unittest


class ClientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = []
        cls.table = "countries"
        cls.url = os.getenv("SUPABASE_URL")
        cls.key = os.getenv("SUPABASE_KEY")
        cls.schema = os.getenv("SUPABASE_TEST_SCHEMA", "public")

    def tearDown(self):
        for row in self.rows:
            self.client.table(self.table).delete().eq("id", row.get('id')).execute() # pylint: disable=no-member
        self.rows.clear()
