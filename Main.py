import json
import random

DICTIONARY_FILE_PATH = 'dictionary.json'
STAGES_FILE_PATH = 'stages.json'
ENCODING = 'utf-8'

def get_dictionary() -> list[str]:
    with open(DICTIONARY_FILE_PATH, 'r', encoding=ENCODING) as file:
        dictionary = json.load(file)
    return dictionary


def get_random_word() -> str:
    dictionary = get_dictionary()
    return random.choice(dictionary)


def get_hangman_stages() -> list[str]:
    with open(STAGES_FILE_PATH, 'r', encoding=ENCODING) as file:
        stages = json.load(file)
    return stages


def print_hangman(tries: int):
    stages = get_hangman_stages()

    if 0 <= tries < len(stages):
        print(stages[tries])
    else:
        print("Invalid stage number")


def print_greeting():
    print('Игра "Виселица" начинается...')
    print('Слово загадано. Угадайте его!', end='\n\n')


def print_goodbye(word: str, win: bool):
    print(f'Загаданное слово {word}')
    if win:
        print('Игра закончена, вы выиграли! =)', end='\n\n')
    else:
        print('Игра закончена, вы проиграли! =(', end='\n\n')


def update_mask(word: str, mask: list[bool], char: str) -> list[bool]:
    if len(char) != 1:
        print("Invalid char")
    for i in range(len(word)):
        if word[i] == char:
            mask[i] = True
    return mask


def print_word(word: str, mask: list[bool]):
    for i in range(len(word)):
        if mask[i]:
            print(word[i], end=' ')
        else:
            print('*', end=' ')
    print()


def ask_ru_char() -> chr:
    print("Введите букву: ")
    user_input = input().lower()
    while not is_ru_char(user_input):
        print("Введите корректную букву (А-Я / а-я): ")
        user_input = input().lower()
    return user_input

def is_ru_char(char)  -> bool:
    return len(char) == 1 and 1040 < ord(char) < 1104


def ask_next_game() -> bool:
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
    max_tries = 6
    win = False

    print_word(word, mask)
    while max_tries >= 0:
        ch = ask_ru_char()
        if ch in word:
            print("Есть такая буква")
            mask = update_mask(word, mask, ch)
            print_word(word, mask)
        else:
            print("Нет такой буквы")
            print_hangman(stage)
            stage += 1
            max_tries -= 1
            print_word(word, mask)

        if mask.count(False) == 0:
            win = True
            break

    print_goodbye(word, win)

while ask_next_game():
    main()