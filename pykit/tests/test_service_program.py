import unittest
import os
from pykit.transport.http import connect
from pykit import Character, ServiceProgram, Integer, Float


class TestServiceProgram(unittest.TestCase):
    def setUp(self):
        char = Character("char", 128, "Hi there")
        self.hello_prog = ServiceProgram("HELLOSRV", "DB2JSON", "HELLO")
        self.hello_prog.add_parameter(char)

    def test_hello(self):
        self.assertEqual(
            self.hello_prog.get_payload(),
            {"pgm":[{"name":"HELLOSRV",  "lib":"DB2JSON", "func": "HELLO"}, {"s":{"name":"char", "type":"128a", "value":"Hi there"}}]}
        )

    def test_execute_hello_world(self):
        connection = connect(
            os.environ['PK_DB2SOCK_URL'],
            db2sock_auth=(
                os.environ['PK_DB2SOCK_USER'], os.environ['PK_DB2SOCK_PASS']))
        toolkit = connection.toolkit()
        toolkit.add(self.hello_prog)
        response = toolkit.execute()
        self.assertEqual(response, {"script": [{"pgm": ["HELLOSRV", "DB2JSON", "HELLO", {"char": "Hello World"}]}]})


if __name__ == '__main__':
    unittest.main()
