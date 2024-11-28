def nfs(row, col, matrix, visited):
    pass


rows = int(input())
cols = int(input())
matrix = []
visited = []

for i in range(rows):
    matrix.append(list(input()))
    matrix.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        
        nfs(row, col, matrix, visited)

for i in matrix:
    print(i)
