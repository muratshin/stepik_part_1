from random import *


def greets():
    print(
        "\n"
        "Приветствую Вас генераторе паролей! \n"
        "Ответьте на нижеследующие вопросы для формирования пароля."
    )


def chars_gen(elem: bool):
    digits = "0123456789"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!#$%&*+-=?@^_"
    unwanted_simbols = "il1Lo0O"

    if not elem:  # Удаление неоднозначных символов
        for i in unwanted_simbols:
            digits = digits.replace(i, "")
            upper_case = upper_case.replace(i, "")
            lower_case = lower_case.replace(i, "")

    return digits, upper_case, lower_case, symbols


def is_digit_valid(request, n):
    while not request.isdigit() or int(request) < n:
        request = input(f"Некорректный ввод. Введите число от {n}: ")

    return int(request)


def is_request_valid(request):
    while request.lower() not in ["да", "нет", "lf", "ytn"]:
        request = input("Некорректный ответ. Введите (Да / Нет): ")
    if request.lower() in ["да", "lf"]:
        return True
    else:
        return False


def pass_geneneration(length_pass: int, answers: list, chars: list):
    password = []
    # Исключаем ответ с использованием неоднозначных символов
    counter = sum(answers[:-1])
    pool = "".join([chars[i] for i in range(4) if answers[i]])

    for i in range(4):  # С гарантированным наличием символов из каждой группы
        if answers[i]:
            for j in range(length_pass // counter):
                password.append(choice(chars[i]))

    for k in range(length_pass % counter):
        password.append(choice(pool))

    shuffle(password)

    return password


def main():
    chars_for_password = []  # Список используемых символов
    settings = []  # Список значений по вопросам
    questions = [
        "3. Использовать цифры? (Да / Нет) ",
        "4. Использовать прописные буквы? (Да / Нет) ",
        "5. Использовать строчные буквы? (Да / Нет) ",
        '6. Использовать символы "!#$%&*+-=?@^_"? (Да / Нет) ',
        '7. Использовать неоднозначные символы "il1Lo0O"? (Да / Нет) ',
    ]
    greets()
    count_of_passwords = is_digit_valid(
        input("1. Введите необходимое количество паролей: "), 1
    )
    length_of_password = is_digit_valid(
        input("2. Введите необходимую длину пароля: "), 8
    )
    for i in range(5):
        settings.append(is_request_valid(input(f"{questions[i]}")))

    chars_for_password.extend(chars_gen(settings[4]))  # Генерация списка символов

    print("\nВывожу сгенерированные пароли:\n")

    for _ in range(count_of_passwords):
        print(
            *pass_geneneration(length_of_password, settings, chars_for_password), sep=""
        )


main()  # Старт программы
