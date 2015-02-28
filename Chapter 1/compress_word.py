def compress(word):
    compressed = []
    current_letter = word[0]
    counter = 0

    for letter in word:
        if letter == current_letter:
            counter += 1
        else:
            compressed.append(current_letter)
            compressed.append(str(counter))

            current_letter = letter
            counter = 1

    #add last sequence
    compressed.append(current_letter)
    compressed.append(str(counter))

    compressed = ''.join(compressed)

    if len(compressed) > len(word):
        return word
    else:
        return compressed


if __name__ == '__main__':
    word1 = 'aabcccccaaa'
    word2 = 'abcdef'

    print('original: %s' % word1)
    print('compressed: %s' % compress(word1))

    print('original: %s' % word2)
    print('compressed: %s' % compress(word2))
