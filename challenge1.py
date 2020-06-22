def letter_stairs(letter, wide, tall):
    temp = 0
    x = " "
    w = int(wide/tall)
    for i in range(0, tall):
        print(temp*x + letter)
        temp += w


if __name__ == '__main__':
    try:
        letter = input('Please input one letter: ')
        wide = int(input('Please input wide: '))
        tall = int(input('Please input tall: '))
        if letter.isalpha():
            a = list(letter)
            if len(a) == 1:
                letter_stairs(letter, wide, tall)
            else:
                print('Please input the correct letter and numbers')
        else:
            print('Please input the correct letter and numbers')
    except ValueError:
        print('Please input the correct letter and numbers')