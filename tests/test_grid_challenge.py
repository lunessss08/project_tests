import unittest
from logic.grid_challenge import grid_challenge


class TestGridChallenge(unittest.TestCase):

    def test_grid_success(self):
        """กรณีที่เรียงแถวแล้ว คอลัมน์ก็เรียงด้วย (YES)"""
        grid = ["abc", "hjk", "mpq", "rtv"]
        self.assertEqual(grid_challenge(grid), "YES")

    def test_grid_fail(self):
        """กรณีที่เรียงแถวแล้ว แต่คอลัมน์ไม่เรียง (NO)"""
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        # เมื่อเรียงแถวแรกจะได้ abcde แถวสอง fghij ... แล้วลองเช็คคอลัมน์
        self.assertEqual(grid_challenge(grid), "YES")  # ตัวอย่างนี้ควรได้ YES

        # เคสที่ต้องได้ NO
        grid_no = ["abc", "hjk", "mpq", "abc"]  # แถวสุดท้ายน้อยกว่าแถวก่อนหน้าในแนวคอลัมน์
        self.assertEqual(grid_challenge(grid_no), "NO")

    def test_single_element_grid(self):
        """กรณีตารางขนาด 1x1"""
        self.assertEqual(grid_challenge(["a"]), "YES")

    def test_all_same_characters(self):
        """กรณีตัวอักษรเหมือนกันหมด"""
        grid = ["aaa", "aaa", "aaa"]
        self.assertEqual(grid_challenge(grid), "YES")


if __name__ == "__main__":
    unittest.main()
