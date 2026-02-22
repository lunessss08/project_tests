def grid_challenge(grid):
    # 1. เรียงลำดับตัวอักษรในแต่ละแถว
    sorted_grid = []
    for row in grid:
        sorted_grid.append("".join(sorted(row)))

    rows = len(sorted_grid)
    cols = len(sorted_grid[0])

    # 2. ตรวจสอบแต่ละคอลัมน์ว่าเรียงจากน้อยไปมากหรือไม่
    for c in range(cols):
        for r in range(rows - 1):
            if sorted_grid[r][c] > sorted_grid[r + 1][c]:
                return "NO"

    return "YES"
