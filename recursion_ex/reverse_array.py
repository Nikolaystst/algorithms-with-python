def rev_arr(array_1, array_2):
    if len(array_1) == 0:
        return array_2
    el = array_1.pop()
    array_2.append(el)
    rev_arr(array_1, array_2)


arr_1 = input().split()
arr_2 = []

rev_arr(arr_1, arr_2)

print(' '.join(arr_2))
