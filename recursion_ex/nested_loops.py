def nested_loops(idx, array):
    if idx >= len(array):
        print(*array, sep=' ')
        return
    for num in range(1, len(array) + 1):
        array[idx] = num
        nested_loops(idx + 1, array)


n = int(input())
list_of_nums = [None] * n

nested_loops(0, list_of_nums)
