def count(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    score = 0
    score += count(row + 1, col, rows, cols)
    score += count(row, col + 1, rows, cols)

    return score


rows = int(input())
cols = int(input())

print(count(0, 0, rows, cols))
