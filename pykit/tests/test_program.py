import unittest
import os
from pykit.transport.http import connect
from pykit import Character, Program


class TestCharacter(unittest.TestCase):
    def setUp(self):
        char = Character(128, "Hi there")
        self.hello_prog = Program("HELLO", "DB2JSON")
        self.hello_prog.addParameter(char)

    def test_hello_world(self):
        self.assertEqual(
            self.hello_prog.get_payload(),
            {"pgm":[{"name":"HELLO",  "lib":"DB2JSON"}, {"s":{"name":"char", "type":"128a", "value":"Hi there"}}]}
        )

    def test_execute_hello_world(self):
        connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(
                os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))
        toolkit = connection.toolkit()
        toolkit.add(self.hello_prog)
        response = toolkit.execute()
        self.assertEqual(response, {"script": [{"pgm": ["HELLO", "DB2JSON", {"char": "Hello World"}]}]})


if __name__ == '__main__':
    unittest.main()
