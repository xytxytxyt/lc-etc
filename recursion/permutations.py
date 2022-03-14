# ctci edition 6 pg 355

def without_i(s, i):
    return s[:i] + s[(i + 1):]


def permutations(s):
    results = set()
    permutations_helper(s, '', results)
    return results


def permutations_helper(s, so_far=None, results=None):
    if so_far is None:
        so_far = ''
    if results is None:
        results = set()
    if len(s) == 1:
        results.add(so_far + s)
        return
    else:
        for i in range(len(s)):
            permutations_helper(without_i(s, i), so_far + s[i], results)
    return


if __name__ == '__main__':
    assert(permutations('a') == {'a'})
    assert(permutations('ab') == {'ab', 'ba'})
    assert(permutations('abc') == {
        'abc',
        'acb',
        'bac',
        'bca',
        'cab',
        'cba',
    })
