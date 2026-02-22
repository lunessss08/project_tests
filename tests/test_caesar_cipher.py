import unittest
from logic.caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):

    def test_basic_rotation(self):
        # """ทดสอบการเลื่อนตัวอักษรปกติแบบไม่วนรอบ"""
        self.assertEqual(caesar_cipher("abc", 3), "def")
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")

    def test_wrap_around(self):
        # """ทดสอบการเลื่อนที่วนกลับจาก z ไป a"""
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

    def test_large_k(self):
        # """ทดสอบกรณีค่า k มากกว่า 26 (ต้องใช้ modulo)"""
        # 87 % 26 = 9 ดังนั้น 'A' เลื่อน 9 ตำแหน่งเป็น 'J'
        self.assertEqual(caesar_cipher("A", 87), "J")

    def test_non_alphabetic(self):
        # """ทดสอบว่าตัวเลขและสัญลักษณ์ต้องไม่เปลี่ยน"""
        self.assertEqual(caesar_cipher("15-pb!", 2), "15-rd!")

    def test_empty_string(self):
        # """ทดสอบกรณีสตริงว่าง (Edge Case)"""
        self.assertEqual(caesar_cipher("", 5), "")

    def test_mixed_case_with_symbols(self):
        # """ทดสอบกรณีผสม (ปรับให้ตรงกับ Logic การเลื่อน 2 ตำแหน่งจริง)"""
        original = "middle-Outz"
        # z + 2 ตำแหน่ง ต้องได้ b (z -> a -> b)
        expected = "okffng-Qwvb"
        self.assertEqual(caesar_cipher(original, 2), expected)


if __name__ == "__main__":
    unittest.main()
