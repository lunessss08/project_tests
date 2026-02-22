def funny_string(s):
    r = s[::-1]
    n = len(s)
    for i in range(1, n):
        # คำนวณหาค่าสัมบูรณ์ของผลต่าง ASCII
        diff_s = abs(ord(s[i]) - ord(s[i - 1]))
        diff_r = abs(ord(r[i]) - ord(r[i - 1]))
        if diff_s != diff_r:
            return "Not Funny"
    return "Funny"
