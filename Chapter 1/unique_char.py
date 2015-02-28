def isUniqueChars(string):
    return len(string) == len(set(string))

if __name__ == "__main__":
    word1 = 'abcde'
    word2 = 'aabbcc'

    assert isUniqueChars(word1)
    assert not isUniqueChars(word2)
