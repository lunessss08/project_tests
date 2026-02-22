import unittest
from logic.two_characters import alternate


class TestTwoCharacters(unittest.TestCase):

    def test_basic_case(self):
        """ทดสอบกรณีปกติจากโจทย์ HackerRank: beabeefeab"""
        # ถ้าเลือก 'a' และ 'b' จะได้ 'abab' ยาว 4
        # ถ้าเลือก 'e' และ 'f' จะได้ 'efe' ยาว 3
        self.assertEqual(
            alternate("beabeefeab"), 5
        )  # เคสนี้ผลลัพธ์สูงสุดคือ 'babab' จาก 'a' และ 'f' ถูกลบออก

    def test_no_alternating_possible(self):
        """ทดสอบกรณีที่ไม่สามารถสร้างสตริงสลับได้เลย"""
        self.assertEqual(alternate("aaaaa"), 0)

    def test_two_unique_chars_already_alternating(self):
        """ทดสอบกรณีที่มี 2 ตัวอยู่แล้วและสลับกันอยู่แล้ว"""
        self.assertEqual(alternate("ababab"), 6)

    def test_two_unique_chars_not_alternating(self):
        """ทดสอบกรณีที่มี 2 ตัวแต่ไม่สลับกัน (มีตัวซ้ำติดกัน)"""
        self.assertEqual(alternate("abaabb"), 0)

    def test_single_char(self):
        """ทดสอบกรณีมีตัวอักษรเดียว (Edge Case)"""
        self.assertEqual(alternate("a"), 0)

    def test_empty_string(self):
        """ทดสอบกรณีสตริงว่าง"""
        self.assertEqual(alternate(""), 0)


if __name__ == "__main__":
    unittest.main()
