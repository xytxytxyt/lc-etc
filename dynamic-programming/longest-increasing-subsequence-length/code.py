# https://www.youtube.com/watch?v=cjWnW0hdF1Y

def longest_increasing_subsequence_length(a):
    # print(a)
    longest_increasing_subsequence_length_starting_at = [1] * len(a)
    first = len(a) - 1
    while first >= 0:
        # print('first', first)
        rest = first + 1
        while rest < len(a):
            # print('rest', rest)
            if a[first] < a[rest]:
                longest_increasing_subsequence_length_starting_at[first] = max(longest_increasing_subsequence_length_starting_at[first], 1 + longest_increasing_subsequence_length_starting_at[rest])
                # print(first, rest, longest_increasing_subsequence_length_starting_at)
            rest += 1
        first -= 1
    return max(longest_increasing_subsequence_length_starting_at)


if __name__ == '__main__':
    assert(longest_increasing_subsequence_length([1, 2, 4, 3]) == 3)
    assert(longest_increasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6)
    assert(longest_increasing_subsequence_length([3, 10, 2, 1, 20]) == 3)
    assert(longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1)
    assert(longest_increasing_subsequence_length([50, 3, 10, 7, 40, 80]) == 4)
    assert(longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
    assert(longest_increasing_subsequence_length([7, 7, 7, 7, 7, 7, 7]) == 1)
