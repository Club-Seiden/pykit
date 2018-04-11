import unittest
import os
from pykit.transport.http import connect


class TestHttpConnection(unittest.TestCase):
    def setUp(self):
        self.connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(
                os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))
        self.toolkit = self.connection.toolkit()

    def test_add_payload(self):
        orig_size = len(self.connection.payload)
        payload = {
            'pgm': [
                {'name': 'HELLO', 'lib': 'DB2JSON'},
                {'s': {'name': 'char', 'type': '128a', 'value': 'Hi there'}}
            ]
        }
        self.toolkit.add(payload)
        self.assertTrue(len(self.connection.payload) - orig_size == 1)

    def test_execute_payload(self):
        response = self.toolkit.execute()
        self.assertEqual(response.ok, True)


if __name__ == '__main__':
    unittest.main()
