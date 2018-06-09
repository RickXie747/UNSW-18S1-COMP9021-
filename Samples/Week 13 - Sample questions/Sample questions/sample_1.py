
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)               

def remove_consecutive_duplicates(word):
    result = []
    for i in len(word):
        if i == len(word) - 1:
            if word[i] != word[i - 1]:
                result.append(word[i])
                return result
            return result
        if word[i] != word[i + 1]:
            result.append(word[i])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
