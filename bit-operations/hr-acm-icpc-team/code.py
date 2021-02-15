import itertools


def get_number_of_subjects(a, b):
    # https://stackoverflow.com/questions/18373563/convert-binary-string-to-binary-literal
    return str(bin(int("0b" + a, 2) | int("0b" + b, 2))).count("1")


def acmTeam(topic):
    combinations = {}
    for c in itertools.combinations(topic, 2):
        n = get_number_of_subjects(c[0], c[1])
        if n not in combinations:
            combinations[n] = 0
        combinations[n] += 1
    max_number = max(combinations.keys())
    return max_number, combinations[max_number]


if __name__ == "__main__":
    topics = [
        "10101",
        "11100",
        "11010",
        "00101",
    ]
    assert(acmTeam(topics) == (5, 2))

    topics = [
        "11101",
        "10101",
        "11001",
        "10111",
        "10000",
        "01110",
    ]
    assert(acmTeam(topics) == (5, 6))
