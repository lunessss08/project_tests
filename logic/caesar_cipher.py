def caesar_cipher(s, k):
    result = ""
    # ใช้ modulo 26 เพื่อรองรับกรณี k > 26 (เช่น k=87)
    shift = k % 26

    for char in s:
        if char.isupper():
            # เลื่อนในขอบเขต A-Z (ASCII 65-90)
            shifted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result += shifted_char
        elif char.islower():
            # เลื่อนในขอบเขต a-z (ASCII 97-122)
            shifted_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result += shifted_char
        else:
            # สัญลักษณ์, ตัวเลข, ช่องว่าง ให้คงเดิม
            result += char

    return result
