from random import *

grey = ["\033[1;30;47m", "\033[0;0;m"]
yellow = ["\033[1;33m", "\033[0;m"]
blue = ["\033[1;30;44m", "\033[0;0;m"]
red = ["\033[1;31m", "\033[0;m"]
full_red = ["\033[1;30;41m", "\033[0;m"]
green = ["\033[1;32m", "\033[0;m"]
full_green = ["\033[1;30;42m", "\033[0;m"]


def get_word():
    word_list = [
        "математика",
        "геометрия",
        "информатика",
        "программирование",
        "питон",
        "образование",
        "телефон",
    ]
    hidden_word = list(choice(word_list).upper())
    return hidden_word


def is_valid_yes_no(request):
    while request.lower() not in ["да", "нет", "lf", "ytn"]:
        request = input("Некорректный ответ. Введите (Да / Нет): ")
    if request.lower() in ["да", "lf"]:
        return True
    else:
        return False


def get_status(cur_word: list, tries_base, tries_cur: int):
    stat = list("o" * tries_cur + "_" * (tries_base - tries_cur))
    print(f"\n{grey[0]} Отгаданные буквы: {grey[1]}", *cur_word, end="")
    print(f" {grey[0]} Осталось попыток: {grey[1]}", *stat)
    # print("\n\033[1;30;47m Отгаданные буквы: \033[0;0;m", *cur_word, end="")
    # print(" \033[1;30;47m Осталось попыток: \033[0;0;m", *stat)


def is_char_valid(request: str):  # Отсечка по регистру
    key = list("абвгдежзийклмнопрстуфхцчшщъыьэюя")
    flag = False
    while not flag:
        for i in request.lower():
            if i in key:
                flag = True

            else:
                flag = False
                request = input(
                    "Некорректный ввод. Введите букву или слово целиком кириллицей: "
                )
                break

    return True, request  # Возвращает, если запрос кириллицей


def is_request_valid(req: str, wrd_len: int):  # Отсечка по регистру и длине слова
    flag, req = is_char_valid(req)

    while not flag or not (len(req) in [1, wrd_len]):
        flag, req = is_char_valid(
            input("Некорректный ввод. Введите букву или слово целиком кириллицей: ")
        )

    return req.upper()


def start_game(chars_help: bool, tries_base: int):
    hid_word = get_word()  # Генерация загаданного слова
    # Начальный уровень попыток // Длина загаданного слова
    tries, len_hid_word = tries_base, len(hid_word)
    cur_word, guess_player = list("_" * len_hid_word), list()
    print("\nTEST///", *hid_word, "///TEST")
    print(f"\n{blue[0]}Угадайка началась!{blue[1]}")

    if chars_help:  # Открытие первой и последней буквы
        cur_word[0] = hid_word[0]
        cur_word[-1] = hid_word[-1]

    while tries != 0:  # Основной цикл
        if cur_word.count("_") == 0:
            print(f"\n{full_green[0]}Отлично, Вы угадали слово!{full_green[1]}")
            get_status(cur_word, tries_base, tries)
            break

        get_status(cur_word, tries_base, tries)
        guess = is_request_valid(
            input("\nВведите букву или слово целиком кириллицей: "), len_hid_word
        )
        if guess in guess_player:
            print(f"\n{yellow[0]}Вы уже вводили подобный запрос.{yellow[1]}")
            continue

        elif len(guess) == 1:  # Если введена буква
            guess_player.append(guess)
            if hid_word.count(guess) != 0:
                print(
                    f"\n{green[0]}Буква {green[1]}{guess}{green[0]} есть в слове!{green[1]}"
                )
                for i in range(len_hid_word):
                    if hid_word[i] == guess:
                        cur_word[i] = guess

                continue

            else:
                guess_player.append(guess)
                tries -= 1
                print(f"\n{red[0]}Буквы {red[1]}{guess}{red[0]} нет в слове.{red[1]}")
                continue

        else:  # Если введено слово
            if guess == "".join(hid_word):
                print(f"\n{full_green[0]}Отлично, Вы угадали слово!{full_green[1]}")
                get_status(hid_word, tries_base, tries)
                break

            else:
                guess_player.append(guess)
                tries -= 1
                print(f"\n{red[0]}Введенное слово не является загаданным{red[1]}")
                continue

    if tries == 0:
        loose = "".join(hid_word)
        print(f"\n{full_red[0]}Не вышло. Загаданное слово: {loose}.{full_red[1]}")


def main():
    print("\nПриветствую Вас в Угадайке слов!\nОпределите нижеследующие настройки:")

    while True:
        tries = 6
        request_1 = is_valid_yes_no(
            input("\nОткрыть первую и последнюю буквы? (Да / Нет) ")
        )
        request_2 = is_valid_yes_no(
            input(
                "\nСтандартное количество попыток 6.\n"
                "Желаете изменить количество попыток? (Да / Нет) "
            )
        )
        if request_2:
            tries = input("\nВведите число попыток: ")
            while not tries.isdigit() or int(tries) < 1:
                tries = input("\nВведите число, большее 1: ")
            tries = int(tries)

        start_game(request_1, tries)  # Запуск игры

        if not is_valid_yes_no(input("\nЖелаете сыграть еще раз? (Да / Нет) ")):
            break

    print("\nЗавершение программы.")


main()
