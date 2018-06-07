import unittest
import os
from pykit.transport.http import connect
from pykit import Character, Program, Integer, Float


class TestCharacter(unittest.TestCase):
    def setUp(self):
        char = Character("char", 128, "Hi there")
        self.hello_prog = Program("HELLO", "DB2JSON")
        self.hello_prog.add_parameter(char)

    def test_hello_world(self):
        self.assertEqual(
            self.hello_prog.get_payload(),
            {"pgm":[{"name":"HELLO",  "lib":"DB2JSON"}, {"s":{"name":"char", "type":"128a", "value":"Hi there"}}]}
        )

    # WIP
    def test_rainbow(self):
        int = Integer("aint8", 3, 1)
        float = Float("afloat", 4, 2, 5.55)
        char = Character("achar", 32, "A")
        rainbow = Program("RAINBOW", "DB2JSON")
        rainbow.add_parameter(int)
        rainbow.add_parameter(float)
        rainbow.add_parameter(char)
        self.assertEqual(
            rainbow.get_payload(),
            {"pgm":[{"name":"RAINBOW",  "lib":"DB2JSON"}, {"s": [
                {"name":"aint8", "type":"3i0", "value":1},
                {"name":"afloat", "type":"4f2", "value":5.55},
                {"name":"achar", "type":"32a", "value":"A"}
            ]}]}
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
