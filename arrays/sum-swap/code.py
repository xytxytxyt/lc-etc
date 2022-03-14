# ctci edition 6 pg 510

def f(a1, a2):
    a1_sum = sum(a1)
    a2_sum = sum(a2)
    a1_d = {}
    for a1_e in a1:
        a1_key = a1_sum - a1_e - a1_e
        a1_d[a1_key] = a1_e
    for a2_e in a2:
        a2_key = a2_sum - a2_e - a2_e
        if a2_key in a1_d:
            return (a1_d[a2_key], a2_e)
    return None


pair_swap_for_equal_sums = f


if __name__ == '__main__':
    assert pair_swap_for_equal_sums([], []) is None
    assert f([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]) == (1, 3)
    assert f([4, 3], [2, 2, 1, 4]) == (3, 4)
    assert f([-3, -3, -3, -3], [2, 3, 4, -7]) == (-3, 4)
