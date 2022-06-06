def sum_of_1_to_n(n):
    return int(n * (n + 1) / 2)


def missing_2(a, n):
    sum_of_missing = sum_of_1_to_n(n) - sum(a)  # O(n)
    avg_of_missing = int(sum_of_missing / 2)
    sum_before_avg = sum([e for e in a if e <= avg_of_missing])  # O(n)
    n_1 = sum_of_1_to_n(avg_of_missing) - sum_before_avg
    n_2 = sum_of_missing - n_1
    return (n_1, n_2)


if __name__ == '__main__':
    assert(missing_2([1, 4, 5], 5) == (2, 3))
    assert(missing_2([1, 3, 4, 6], 6) == (2, 5))
    assert(missing_2([1, 2, 3], 5) == (4, 5))
    assert(missing_2([1, 3, 5], 5) == (2, 4))
