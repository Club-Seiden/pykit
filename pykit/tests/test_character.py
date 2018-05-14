import unittest
import os
from pykit import Character


class TestCharacter(unittest.TestCase):
    def test_character_payload(self):
        char = Character(10, "Hello")
        self.assertEqual(char.get_payload(), {"s":{"name":"char", "type":"10a", "value":"Hello"}})


if __name__ == '__main__':
    unittest.main()
