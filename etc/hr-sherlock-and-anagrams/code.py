# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

import math


def sherlockAndAnagrams(s):
    substrings = {}
    length = 1
    while length < len(s):
        start = 0
        while start + length <= len(s):
            substring = "".join(sorted(s[start:start + length]))
            if substring not in substrings:
                substrings[substring] = 0
            substrings[substring] += 1
            start += 1
        length += 1
    # print(substrings)
    n_pairs = 0
    for substring in substrings:
        n = substrings[substring]
        r = 2
        if n > 1:
            n_pairs += math.factorial(n) // math.factorial(r) // math.factorial(n-r)
    return n_pairs


if __name__ == "__main__":
    assert sherlockAndAnagrams("abba") == 4
    assert sherlockAndAnagrams("abcd") == 0
    assert sherlockAndAnagrams("ifailuhkqq") == 3
    assert sherlockAndAnagrams("ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel") == 399
    assert sherlockAndAnagrams("kaggklnwxoigxncgxnkrtdjnoeblhlxsblnqitdkoiftxnsafukbdhasdeihlhfrqkfzqhvnsmsgnrayhsyjsniutmgpfjmssfsg") == 472
    assert sherlockAndAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 166650
    assert sherlockAndAnagrams("dfcaabeaeeabfffcdbbfaffadcacdeeabcadabfdefcfcbbacadaeafcfceeedacbafdebbffcecdbfebdbfdbdecbfbadddbcec") == 2452
