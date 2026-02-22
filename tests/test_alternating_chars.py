import unittest
from logic.alternating_chars import alternating_characters


class TestAlternatingChars(unittest.TestCase):
    def test_all_same(self):
        # Case: AAAAA -> ลบ 4 ตัวเหลือ A
        self.assertEqual(alternating_characters("AAAAA"), 4)

    def test_already_alternating(self):
        # Case: ABABAB -> ไม่ต้องลบเลย
        self.assertEqual(alternating_characters("ABABAB"), 0)

    def test_mixed_repeats(self):
        # Case: AAABBB -> ลบ AA ออก 2, BB ออก 2 รวมเป็น 4
        self.assertEqual(alternating_characters("AAABBB"), 4)
