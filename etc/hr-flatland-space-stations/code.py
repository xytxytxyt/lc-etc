# https://www.hackerrank.com/challenges/flatland-space-stations/problem

def flatlandSpaceStations(n, c):
    c = sorted(c)
    print("Input: ", n, c)
    d = [c[0]]
    for i in range(len(c) - 1):
        d.append(int((c[i + 1] - c[i]) / 2))
    d.append(n - 1 - c[-1])
    print(d)
    return max(d)


answer = flatlandSpaceStations(100, [93, 41, 91, 61, 30, 6, 25, 90, 97])
expected_answer = 14
assert answer == expected_answer, f"correct answer:\n{expected_answer}\noutput:\n{answer}"


answer = flatlandSpaceStations(20, [13, 1, 11, 10, 6])
expected_answer = 6
assert answer == expected_answer, f"correct answer:\n{expected_answer}\noutput:\n{answer}"
