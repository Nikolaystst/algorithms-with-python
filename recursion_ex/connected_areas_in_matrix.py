rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]
solution = {}
solutions = 1


def explore_the_area(row, col):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'x'
    result = 1

    result += explore_the_area(row + 1, col)
    result += explore_the_area(row - 1, col)
    result += explore_the_area(row, col + 1)
    result += explore_the_area(row, col - 1)

    return result


for row in range(rows):
    for col in range(cols):
        size = explore_the_area(row, col)
        if size:
            solution[solutions] = {'start_point': (row, col), 'size': size}
            solutions += 1

i = 1
print(f'Total areas found: {len(solution)}')
for element in sorted(solution.items(), key=lambda a: (-a[1]['size'], a[0])):
    print(f'Area #{i} at {element[1]['start_point']}, size: {element[1]['size']}')
    i += 1
