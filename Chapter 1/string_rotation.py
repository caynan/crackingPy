def isRotation(s1, s2):
    s1s1 = s1 + s1
    return s2 in s1s1

if __name__ == '__main__':
    assert isRotation('waterbottle', 'erbottlewat')

