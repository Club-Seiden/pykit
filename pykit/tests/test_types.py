import unittest
import os
from pykit import Integer, Float, Character, Decimal, Binary


class TestInteger(unittest.TestCase):
    def test_integer_payload(self):
        new_int = Integer('aint8', 3, 1)
        self.assertEqual(new_int.get_payload(), {"name":"aint8", "type":"3i0", "value":1})

    def test_unsigned_integer_payload(self):
        new_int = Integer('auint8', 3, 1, False)
        self.assertEqual(new_int.get_payload(), {"name":"auint8", "type":"3u0", "value":1})


class TestFloat(unittest.TestCase):
    def test_float_payload(self):
        new_float = Float('afloat', 4, 2, 5.55)
        self.assertEqual(new_float.get_payload(), {"name":"afloat", "type":"4f2", "value":5.55})


class TestCharacter(unittest.TestCase):
    def test_character_payload(self):
        char = Character('achar', 10, "Hello")
        self.assertEqual(char.get_payload(), {"name":"achar", "type":"10a", "value":"Hello"})

    def test_character_varying_payload(self):
        char = Character('bchar', 100, "Bye", 2)
        self.assertEqual(char.get_payload(), {"name":"bchar", "type":"10av2", "value":"Bye"})


class TestDecimal(unittest.TestCase):
    def test_decimal_payload(self):
        dec = Decimal('adec', 10, 2, 850.2)
        self.assertEqual(dec.get_payload(), {"name":"adec", "type":"10p2", "value":850.2})

    def test_signed_decimal_payload(self):
        dec = Decimal('bdec', 9, 0, 800, True)
        self.assertEqual(dec.get_payload(), {"name":"bdec", "type":"9p0", "value":800})

class TestBinary(unittest.TestCase):
    def test_binary_payload(self):
        bin = Binary('abin', 2, 0000)
        self.assertEqual(bin.get_payload(), {"name":"abin", "type":"2b", "value":"0000"})



if __name__ == '__main__':
    unittest.main()
