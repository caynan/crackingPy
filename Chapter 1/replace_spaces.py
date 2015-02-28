def replace_space(string):
    return string.strip().replace(' ', '%20')

if __name__ == '__main__':
    string = '   O   rato  roeu a roupa do rei de roma   !  '
    print('original: %s' % string)
    print('replaced: %s' % replace_space(string))
