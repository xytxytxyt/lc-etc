import heapq


def kth_largest(a, k):
    h = []
    for e in a:
        heapq.heappush(h, e)  # O(log k) because heap is of size k
        if len(h) > k:
            heapq.heappop(h)  # O(log k)
    return h[0]
    # total O(n log k) because we push n elements onto the heap


def test_array(a, k):
    result = kth_largest(a, k)
    expected = sorted(a, reverse=True)[k - 1]
    print('a', a, 'k', k, 'result', result, 'expected', expected)
    assert(result == expected)


if __name__ == '__main__':
    test_array([1, 2, 3, 4, 5, 6], 4)
    test_array([3, 2, 1, 5, 6, 4], 2)
    test_array([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    test_array([1, 23, 12, 9, 30, 2, 50], 3)
