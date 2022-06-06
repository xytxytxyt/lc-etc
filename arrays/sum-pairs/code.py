def sum_pairs(a, k):
    s = set()
    pairs = []
    for e in a:
        other_e = k - e
        if other_e in s:
            pairs.append((e, other_e))
        s.add(e)
    return pairs


if __name__ == '__main__':
    assert(sum_pairs([1, 2, 3, 4, 5, 6], 5) == [(3, 2), (4, 1)])
    assert(sum_pairs([1, 2, 3, 3, 4], 6) == [(3, 3), (4, 2)])
    assert(sum_pairs([1, 2, 3, 3, 4], 5) == [(3, 2), (3, 2), (4, 1)])
    assert(sum_pairs([1, 2, 3, 4, 5], 17) == [])
