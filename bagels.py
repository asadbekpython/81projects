"""
Bagels
Дедуктивная логическая игра на угадывание числа-букв по подсказкам.
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 30

def main():
    """Оснавная функция"""

    print(f'''
    Bagels, a deductive logic game.

    I am thinking of a {NUM_DIGITS}-digit number-letter with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:           That means:
     Pico                  One digit is correct but in the wrong position.
     Fermi                 One digit is correct and in the right pocition.
     Bagels                No digit is correct.

    For example, if the secret number-letter was h48 and your guess was 84l, the
    clues would be Fermi Pico.\n
    ''')

    while True:
        print("I have thought up a number-letter.")
        print(f"You have {MAX_GUESSES} guesses to get it.\n\n")
        secretNum = getSecretNum()

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:

            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isalnum():
                print(f'Guess number #{numGuesses}')
                guess = input('> ')

            clue = getClues(guess, secretNum)
            print(clue)
            numGuesses += 1

            print('-------------\n')
            if secretNum == guess:
                break
            if numGuesses > MAX_GUESSES:
                print('You do not have guesses')
                print('You lose :(')
                print(f'The secret number-letter was {secretNum}')


        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for game!!!')


def getSecretNum():
    """Функция, которая генерирует случайное трехзначное строковое число"""
    numbers = list('0123456789qwertyuiopasdfghjklzxcvbnm')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += numbers[i]
    return secretNum

def getClues(guess, secretNum):
    """Функция, которая в зависимости от входных данных возвращает подсказки"""
    if guess == secretNum:
        return '\n!!!You win!!!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append("Pico")

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


if __name__ == '__main__':
    main()
