# Stepik UGADAIKA
from random import *
from time import *


def greets():
    print(
        '\nПриветствую Вас в "Числовой угадайке"! \nКомпьютер загадывает число в диапазоне от 1 до 100.'
    )


def again():
    ag = input("\nЖелаете повторить игру? (Да / Нет): ")
    while ag.lower() not in ["да", "нет", "lf", "ytn"]:
        ag = input("Некорректный ответ. Введите (Да / Нет): ")
    if ag.lower() in ["да", "lf"]:
        return True
    else:
        return False


def choose():
    start_r, end_r = 1, 100
    ch = input("\nЖелаете изменить диапазон значений? (Да / Нет): ")
    while ch.lower() not in ["да", "нет", "lf", "ytn"]:
        ch = input("Некорректный ответ. Введите (Да / Нет): ")

    if ch.lower() in ["да", "lf"]:
        start_r = input("Введите начало диапазона: ")
        while not start_r.isdigit():
            start_r = input("Это должно быть число. Введите заново: ")

        end_r = input("Введите конец диапазона: ")
        while not end_r.isdigit() or int(end_r) <= int(start_r):
            end_r = input(f"Это должно быть число, большее {start_r}. Введите заново: ")

    elif ch.lower() in ["нет", "ytn"]:
        print("Принято. Диапазон остается стандартным.")

    return int(start_r), int(end_r)


def valid(start_r, end_r):
    n = input("\nВведите предполагаемое число: ")
    while not (n.isdigit() and start_r <= int(n) <= end_r):
        n = input(
            f"Не соответствует формату, число должно быть в диапазоне [{start_r};{end_r}].\nВведите заново: "
        )

    return int(n)


def game_pc(start_r, end_r):  # против компьютера
    key, counter = randint(start_r, end_r), 1
    flag = True
    print(f"\nОтладка ключ: {key}.")
    req = valid(start_r, end_r)

    while flag:
        if req > key:
            counter += 1
            print("\nНет. Загаданное число меньше введенного.")
            req = valid(start_r, end_r)

        elif req < key:
            counter += 1
            print("\nНет. Загаданное число больше введенного.")
            req = valid(start_r, end_r)

        else:
            flag = False

    print(f"Верно! Количество попыток: {counter}.")


def main():
    flag = True
    greets()
    sleep(0.5)
    # n_start, n_end = choose()
    # game_pc(n_start, n_end)
    while flag:
        n_start, n_end = choose()
        sleep(0.5)
        game_pc(n_start, n_end)
        flag = again()

    print("\nСпасибо Вам большое, за уделенное время!")


main()

# req = input('Введите предполагаемое число: ')
