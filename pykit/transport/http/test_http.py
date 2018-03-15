import unittest
import os
from . import connect


class TestHttpConnection(unittest.TestCase):
    def setUp(self):
        self.connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))

    def test_url_is_set(self):
        self.assertEqual(self.connection.db2sock_rest_url, os.environ['PK_DB2SOCK_URL'])

    def test_auth_is_set(self):
        self.assertEqual(
            self.connection.db2sock_auth, (os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))


if __name__ == '__main__':
    unittest.main()
