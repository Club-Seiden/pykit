import unittest
import os
from pykit import Float


class TestFloat(unittest.TestCase):
    def test_float_payload(self):
        new_float = Float('afloat', 4, 2, 5.55)
        self.assertEqual(new_float.get_payload(), {"name":"afloat", "type":"4f2", "value":5.55})


if __name__ == '__main__':
    unittest.main()
