def isPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    # case 1
    str1 = 'amor'
    str2 = 'roma'

    assert isPermutation(str1, str2)

    # case 2
    str1 = 'lagosta'
    str2 = 'abobora'
    assert not isPermutation(str1, str2)

