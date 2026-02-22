def alternate(s):
    max_len = 0
    # 1. หาตัวอักษรที่ไม่ซ้ำกัน
    unique_chars = list(set(s))

    # 2. ลองจับคู่ตัวอักษรทุกคู่ที่เป็นไปได้
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]

            # 3. สร้างสตริงใหม่ที่มีแค่ 2 ตัวที่เลือก
            filtered_s = [c for c in s if c == char1 or c == char2]

            # 4. ตรวจสอบว่าสลับกัน (Alternating) หรือไม่
            is_alternating = True
            for k in range(len(filtered_s) - 1):
                if filtered_s[k] == filtered_s[k + 1]:
                    is_alternating = False
                    break

            # 5. ถ้าสลับกัน ให้บันทึกความยาวที่มากที่สุด
            if is_alternating:
                max_len = max(max_len, len(filtered_s))

    return max_len
