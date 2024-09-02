import json
import random

DICTIONARY_FILE_PATH = 'dictionary.json'
STAGES_FILE_PATH = 'stages.json'
ENCODING = 'utf-8'

def get_dictionary():
    with open(DICTIONARY_FILE_PATH, 'r', encoding=ENCODING) as file:
        dictionary = json.load(file)
    return dictionary

def get_random_word():
    dictionary = get_dictionary()
    return random.choice(dictionary)


def get_hangman_stages():
    with open(STAGES_FILE_PATH, 'r', encoding=ENCODING) as file:
        stages = json.load(file)
    return stages


def print_hangman(tries):
    stages = get_hangman_stages()

    if 0 <= tries < len(stages):
        print(stages[tries])
    else:
        print("Invalid stage number")


def print_greeting():
    print('Игра "Виселица" начинается...')
    print('Слово загадано. Угадайте его!', end='\n\n')

def print_goodbye(word, win):
    print(f'Загаданное слово {word}')
    if win:
        print('Игра закончена, вы выиграли! =)')
    else:
        print('Игра закончена, вы проиграли! =(')


def update_mask(word, mask, char):
    for i in range(len(word)):
        if word[i] == char:
            mask[i] = True
    return mask


def print_word(word, mask):
    for i in range(len(word)):
        if mask[i]:
            print(word[i], end=' ')
        else:
            print('*', end=' ')
    print()


def ask_char():
    print("Введите букву: ")
    user_input = input().lower()
    while user_input.isalpha() == False or len(user_input) != 1:
        print("Введите корректную букву: ")
        user_input = input().lower()
    return user_input

def ask_next_game():
    print("Хотите сыграть в игру? (да/нет)")
    inp = input()

    while True:
        if inp == 'да':
            return True
        elif inp == 'нет':
            return False
        else:
            print("Введите корректный ответ (да/нет): ")
            inp = input()


def main():
    print_greeting()

    stage = 0
    word = get_random_word()
    mask = [False] * len(word)
    max_tries = len(word)

    print_word(word, mask)
    while max_tries > 0:
        ch = ask_char()
        if ch in word:
            print("Есть такая буква")
            mask = update_mask(word, mask, ch)
            print_word(word, mask)
        else:
            print("Нет такой буквы")
            stage += 1
            print_hangman(stage)
            print_word(word, mask)

        max_tries -= 1
        if mask.count(False) == 0:
            print_goodbye(word, True)

    print_goodbye(word, False)


while ask_next_game():
    main()