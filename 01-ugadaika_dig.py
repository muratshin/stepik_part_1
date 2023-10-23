# Stepik UGADAIKA
from random import *
from time import *


def greets():
    print(
        "\n"
        'Приветствую Вас в "Числовой угадайке"! \n'
        "Компьютер загадывает число в диапазоне от 1 до 100."
    )


def ask_user_to_play_again():
    play_again = input("\nЖелаете повторить игру? (Да / Нет): ")
    while play_again.lower() not in ["да", "нет", "lf", "ytn"]:
        play_again = input("Некорректный ответ. Введите (Да / Нет): ")
    if play_again.lower() in ["да", "lf"]:
        return True
    else:
        return False


def ask_user_for_game_parameters():
    start_range, end_range = 1, 100
    ch = input("\nЖелаете изменить диапазон значений? (Да / Нет): ")
    while ch.lower() not in ["да", "нет", "lf", "ytn"]:
        ch = input("Некорректный ответ. Введите (Да / Нет): ")

    if ch.lower() in ["да", "lf"]:
        start_range = input("Введите начало диапазона: ")
        while not start_range.isdigit():
            start_range = input("Это должно быть число. Введите заново: ")

        end_range = input("Введите конец диапазона: ")
        while not end_range.isdigit() or int(end_range) <= int(start_range):
            end_range = input(
                f"Это должно быть число, большее {start_range}. Введите заново: "
            )

    elif ch.lower() in ["нет", "ytn"]:
        print("Принято. Диапазон остается стандартным.")

    return int(start_range), int(end_range)


def valid(start_range, end_range):
    n = input("\nВведите предполагаемое число: ")
    while not (n.isdigit() and start_range <= int(n) <= end_range):
        n = input(
            f"Не соответствует формату, число должно быть в диапазоне [{start_range};{end_range}].\n"
            "Введите заново: "
        )

    return int(n)


def game_pc(start_range, end_range):  # против компьютера
    key, counter = randint(start_range, end_range), 1
    flag = True
    print(f"\nОтладка ключ: {key}.")
    req = valid(start_range, end_range)

    while flag:
        if req > key:
            counter += 1
            print("\nНет. Загаданное число меньше введенного.")
            req = valid(start_range, end_range)

        elif req < key:
            counter += 1
            print("\nНет. Загаданное число больше введенного.")
            req = valid(start_range, end_range)

        else:
            flag = False

    print(f"Верно! Количество попыток: {counter}.")


def main():
    flag = True
    greets()
    sleep(0.5)

    while flag:
        range_start, range_end = ask_user_for_game_parameters()
        sleep(0.5)
        game_pc(range_start, range_end)
        flag = ask_user_to_play_again()

    print("\nСпасибо Вам большое, за уделенное время!")


main()
