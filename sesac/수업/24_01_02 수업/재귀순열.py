arr = ['A', 'B', 'C']
arr_len = len(arr)
sel = [0] * arr_len
check = [0] * arr_len

def perm(depth):
    if depth == arr_len:
        print(sel)
        return

    for i in range(arr_len):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0

perm(0)