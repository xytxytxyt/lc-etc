# https://www.hackerrank.com/challenges/almost-sorted/problem

def is_sorted(arr):
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            return False
        i += 1
    return True


def almostSorted(arr):
    if is_sorted(arr):
        print("yes")
        return

    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            break
        i += 1
    l = i - 1
    i = len(arr) - 1
    while i > 1:
        if arr[i] < arr[i - 1]:
            break
        i -= 1
    r = i
    arr_swap = list(arr)
    arr_swap[l], arr_swap[r] = arr_swap[r], arr_swap[l]
    # print("considering swapping", l, r)
    if is_sorted(arr_swap):
        print("yes")
        print(f"swap {l + 1} {r + 1}")
        return

    arr_reverse = list(arr)
    arr_reverse[l:r + 1] = reversed(arr_reverse[l:r + 1])
    # print("considering reversing", l, r)
    if is_sorted(arr_reverse):
        print("yes")
        print(f"reverse {l + 1} {r + 1}")
        return
    else:
        print("no")


almostSorted([4, 2])
print("-")
almostSorted([3, 1, 2])
print("-")
almostSorted([1, 5, 4, 3, 2, 6])
