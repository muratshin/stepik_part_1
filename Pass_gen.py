from random import *


def greets():
    print(
        '\nПриветствую Вас генераторе паролей! \nОтветьте на нижеследующие вопросы для формирования пароля.'
    )


def chars_gen(el):
    dig = '0123456789'
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 'abcdefghijklmnopqrstuvwxyz'
    sim = '!#$%&*+-=?@^_'
    unc = 'il1Lo0O'

    if not el:
        for _ in unc:
            dig = dig.replace(_, '')
            upp = upp.replace(_, '')
            low = low.replace(_, '')

    return dig, upp, low, sim


def choose_dig(req, n):
    while not req.isdigit() or int(req) < n:
        req = input(f"Некорректный ввод. Введите число от {n}: ")

    return int(req)


def choose_yn(req):
    while req.lower() not in ["да", "нет", "lf", "ytn"]:
        req = input("Некорректный ответ. Введите (Да / Нет): ")
    if req.lower() in ["да", "lf"]:
        return True
    else:
        return False


def pass_gen(lp, ans, chrs):  # С гарантированным наличием символов из каждой группы
    password = []
    counter = sum(ans[:-1])  # Исключаем ответ с использованием неоднозначных символов
    pool = ''.join([chrs[i] for i in range(4) if ans[i]])

    if ans[0]:
        for _ in range(lp // counter):
            password.append(choice(chrs[0]))

    if ans[1]:
        for _ in range(lp // counter):
            password.append(choice(chrs[1]))

    if ans[2]:
        for _ in range(lp // counter):
            password.append(choice(chrs[2]))

    if ans[3]:
        for _ in range(lp // counter):
            password.append(choice(chrs[3]))

    for _ in range(lp % counter):
        password.append(choice(pool))

    shuffle(password)

    return password


def settings():
    chars = []  # Список используемых символов
    quest = []  # Список значений по вопросам
    greets()
    qwn = choose_dig(input('1. Введите необходимое количество паролей: '), 1)
    lg = choose_dig(input('2. Введите необходимую длину пароля: '), 8)
    quest.append(choose_yn(input('3. Использовать цифры? (Да / Нет) ')))
    quest.append(choose_yn(input('4. Использовать прописные буквы? (Да / Нет) ')))
    quest.append(choose_yn(input('5. Использовать строчные буквы? (Да / Нет) ')))
    quest.append(choose_yn(input('6. Использовать символы "!#$%&*+-=?@^_"? (Да / Нет) ')))
    quest.append(choose_yn(input('7. Использовать неоднозначные символы "il1Lo0O"? (Да / Нет) ')))

    chars.extend(chars_gen(quest[4]))  # Генерация списка символов

    print('\nВывожу сгенерированные пароли:\n')

    for _ in range(qwn):
        print(*pass_gen(lg, quest, chars), sep='')


settings()  # Старт программы
