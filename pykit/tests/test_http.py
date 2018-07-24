import unittest
import os
from pykit.transport.http import connect


class TestHttpConnection(unittest.TestCase):
    def setUp(self):
        self.connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(
                os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))

    def test_execute_payload(self):
        payload = {
            'pgm': [
                {'name': 'HELLO', 'lib': 'DB2JSON'},
                {'s': {'name': 'char', 'type': '128a', 'value': 'Hi there'}}
            ]
        }
        toolkit = self.connection.toolkit()
        toolkit.add(payload)
        response = toolkit.execute()
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
