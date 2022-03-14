# ctci edition 6 pg 510

def max_subarray(a):
    local_max = float('-inf')
    global_max = float('-inf')
    for i in range(len(a)):
        local_max = max(a[i], a[i] + local_max)
        global_max = max(global_max, local_max)
    return global_max


if __name__ == '__main__':
    assert max_subarray([-1, -2, -3, 4, -2]) == 4
    assert max_subarray([-1, -2, -3]) == -1
    assert max_subarray([2, 3, -8, -1, 2, 4, -2, 3]) == 7
    assert max_subarray([1, 2, 3]) == 6
    assert max_subarray([5, -9, 6, -2, 3]) == -7
