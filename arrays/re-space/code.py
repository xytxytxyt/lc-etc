dictionary = {
    'looked',
    'just',
    'like',
    'her',
    'brother',
}


def respace(s):
    spaced = []
    not_in_dictionary = []
    start = 0
    while start < len(s):
        end = len(s) - 1
        found_in_dictionary = False
        while end > 0:
            word = s[start:(end + 1)]
            if word in dictionary:
                if not_in_dictionary:
                    spaced.append(''.join(not_in_dictionary))
                    not_in_dictionary = []
                spaced.append(word)
                found_in_dictionary = True
                start = end
                break
            end -= 1
        if not found_in_dictionary:
            not_in_dictionary.append(s[start])
        start += 1
    return spaced


if __name__ == '__main__':
    assert(respace('jesslookedjustliketimherbrother') == ['jess', 'looked', 'just', 'like', 'tim', 'her', 'brother'])
