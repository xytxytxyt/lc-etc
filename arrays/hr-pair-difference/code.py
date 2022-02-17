# https://www.hackerrank.com/challenges/pairs/problem

def pairs(k, arr):
    s = set()
    n = 0
    for a in arr:
        x = a - k
        if x > 0 and x in s:
            n += 1
        y = a + k
        if y > 0 and y in s:
            n += 1
        s.add(a)
    return n


if __name__ == "__main__":
    assert(pairs(2, [1, 5, 3, 4, 2])) == 3
    assert(pairs(1, [
        363374326,
        364147530,
        61825163,
        1073065718,
        1281246024,
        1399469912,
        428047635,
        491595254,
        879792181,
        1069262793
    ])) == 0
    assert(pairs(2, [1, 3, 5, 8, 6, 4, 2])) == 5
