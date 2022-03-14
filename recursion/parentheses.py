# ctci edition 6 pg 359

def parentheses(n):
    results = set()
    parentheses_helper(n, n, '', results)
    return results


def parentheses_helper(n_open_left, n_close_left, so_far, results):
    if n_open_left == 0 and n_close_left == 0:
        results.add(so_far)
        return
    if n_open_left > 0:
        parentheses_helper(n_open_left - 1, n_close_left, so_far + '(', results)
    if n_close_left > 0 and n_close_left > n_open_left:
        parentheses_helper(n_open_left, n_close_left - 1, so_far + ')', results)


if __name__ == '__main__':
    assert(parentheses(1) == {'()'})
    assert(parentheses(2) == {'(())', '()()'})
    assert(parentheses(3) == {
        '(()())',
        '((()))',
        '()(())',
        '(())()',
        '()()()',
    })
