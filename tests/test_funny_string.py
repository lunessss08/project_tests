import unittest
from logic.funny_string import funny_string


class TestFunnyString(unittest.TestCase):
    def test_funny_case(self):
        # Case: acxz -> r=zxca | |c-a|=2, |x-c|=21, |z-x|=2 เท่ากันหมด
        self.assertEqual(funny_string("acxz"), "Funny")

    def test_not_funny_case(self):
        # Case: bcxz -> ผลต่างไม่เท่ากันในบางคู่
        self.assertEqual(funny_string("bcxz"), "Not Funny")

    def test_single_char_or_same(self):
        # Boundary Case: ตัวอักษรเหมือนกันหมด
        self.assertEqual(funny_string("aaaaa"), "Funny")
