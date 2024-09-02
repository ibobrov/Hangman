# Виселица

Проект "Виселица" - это консольная игра, в которой игрок должен угадать загаданное слово, вводя буквы по одной. Если игрок угадывает букву, она отображается в слове. Если нет, игрок теряет попытку, и на экране отображается часть виселицы. Игра продолжается до тех пор, пока игрок не угадает слово или не исчерпает все попытки.

## Установка

1. **Клонируйте репозиторий:**
   ```sh
   git clone https://github.com/ibobrov/hangman.git
   cd hangman
   ```

2. **Создайте виртуальное окружение:**
   ```sh
   python -m venv .venv
   ```

3. **Активируйте виртуальное окружение:**
   - На Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - На macOS и Linux:
     ```sh
     source .venv/bin/activate
     ```

4. **Установите зависимости:**
   ```sh
   pip install -r requirements.txt
   ```

## Запуск

Для запуска игры выполните следующую команду:
```sh
python Main.py
```

## Структура проекта

- `Main.py` - основной файл с логикой игры.
- `dictionary.json` - файл со списком слов для игры.
- `stages.json` - файл с этапами виселицы.
- `.gitignore` - файл с исключениями для Git.

## Правила игры

1. Игра начинается с приветственного сообщения и загадки слова.
2. Игрок вводит буквы по одной.
3. Если буква есть в слове, она отображается на своем месте.
4. Если буквы нет в слове, отображается часть виселицы.
5. Игра продолжается до тех пор, пока игрок не угадает слово или не исчерпает все попытки.

## Пример использования

```sh
python Main.py
```

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле `LICENSE`.