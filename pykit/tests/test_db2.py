import unittest
import os
from pykit.transport.db2 import connect


class TestDb2Connection(unittest.TestCase):
    def setUp(self):
        self.connection = connect('*LOCAL', os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS'])

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
