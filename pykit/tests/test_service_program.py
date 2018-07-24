import unittest
import os
from pykit.transport.http import connect
from pykit import *


class TestServiceProgram(unittest.TestCase):
    def setUp(self):
        char = Character("char", 128, "Hi there")
        char_return = Character("char", 128, "Hi back")
        self.hello_prog = ServiceProgram("HELLOSRV", "DB2JSON", "HELLO")
        self.hello_prog.add_parameter(char)
        self.hello_prog_return = ServiceProgram("HELLOSRV", "DB2JSON", "HELLOAGAIN")
        self.hello_prog_return.add_parameter(char)
        self.hello_prog_return.add_return(char_return)
        

    def test_hello(self):
        self.assertEqual(
            self.hello_prog.get_payload(),
            {"pgm":[{"name":"HELLOSRV",  "lib":"DB2JSON", "func": "HELLO"}, {"s":{"name":"char", "type":"128a", "value":"Hi there"}}]}
        )
        self.assertEqual(
            self.hello_prog_return.get_payload(),
            {"pgm":[{"name":"HELLOSRV",  "lib":"DB2JSON", "func": "HELLOAGAIN"}, {"s":[{"name":"char", "type":"128a", "value":"Hi there"},{"name":"char", "type":"128a", "value":"Hi back", "by":"return"}]}]}
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
