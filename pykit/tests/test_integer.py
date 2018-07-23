import unittest
import os
from pykit import types


class TestInteger(unittest.TestCase):
    def test_integer_payload(self):
        new_int = Integer('aint8', 3, 1)
        self.assertEqual(new_int.get_payload(), {"name":"aint8", "type":"3i0", "value":1})

    def test_unsigned_integer_payload(self):
        new_int = Integer('auint8', 3, 1, False)
        self.assertEqual(new_int.get_payload(), {"name":"auint8", "type":"3u0", "value":1})


if __name__ == '__main__':
    unittest.main()
