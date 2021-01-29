# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

def next_square(n):
    return (int(n**0.5) + 1)**2


def squares(a, b):
    n = a - 1
    number_of_squares = 0
    while True:
        n = next_square(n)
        if n > b:
            break
        number_of_squares += 1
    return number_of_squares


if __name__ == "__main__":
    assert squares(3, 9) == 2
    assert squares(17, 24) == 0
    assert squares(35, 70) == 3
    assert squares(100, 1000) == 22
