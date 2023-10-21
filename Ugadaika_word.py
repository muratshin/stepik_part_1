from random import *


def get_word():
    word_list = ['математика', 'геометрия', 'информатика', 'программирование', 'питон', 'образование', 'телефон']
    hw = list(choice(word_list).upper())
    return hw


def choose_yn(req):
    while req.lower() not in ["да", "нет", "lf", "ytn"]:
        req = input("Некорректный ответ. Введите (Да / Нет): ")
    if req.lower() in ["да", "lf"]:
        return True
    else:
        return False


def status(c_w: list, tr_base, tr_cur: int):
    stat = list('o' * tr_cur + '_' * (tr_base - tr_cur))
    print('\n\033[1;30;47m Отгаданные буквы: \033[0;0;m', *c_w, end='')
    print(' \033[1;30;47m Осталось попыток: \033[0;0;m', *stat)


def valid_char(req: str):  # Отсечка по регистру
    key = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    flag = False
    while not flag:
        for i in req.lower():
            if i in key:
                flag = True

            else:
                flag = False
                req = input('Некорректный ввод. Введите букву или слово целиком кириллицей: 1 ')
                break

    return True, req  # Возвращает, если запрос кириллицей


def valid(req: str, wrd_len: int):  # Отсечка по регистру и длине слова
    flag, req = valid_char(req)

    while not flag or not (len(req) in [1, wrd_len]):
        flag, req = valid_char(input('Некорректный ввод. Введите букву или слово целиком кириллицей: 2 '))

    return req.upper()


def game(ch_he: bool, tr_base: int):
    hid_word = get_word()  # Генерация загаданного слова
    tries, len_h = tr_base, len(hid_word)  # Начальный уровень попыток // Длина загаданного слова
    cur_word, guess_player = list('_' * len_h), list()
    print('\nTEST///', *hid_word, '///TEST')
    print('\n\033[1;30;44mУгадайка началась!\033[0;0;m')

    if ch_he:  # Открытие первой и последней буквы
        cur_word[0] = hid_word[0]
        cur_word[-1] = hid_word[-1]

    while tries != 0:  # Основной цикл
        if cur_word.count('_') == 0:
            print('\n\033[1;30;42mОтлично, Вы угадали слово!\033[0;0;m')
            status(cur_word, tr_base, tries)
            break

        status(cur_word, tr_base, tries)
        guess = valid(input('\nВведите букву или слово целиком кириллицей: '), len_h)
        if guess in guess_player:
            print('\n\033[1;33mВы уже вводили подобный запрос.\033[0;m')
            continue

        elif len(guess) == 1:  # Если введена буква
            guess_player.append(guess)
            if hid_word.count(guess) != 0:
                print(f'\n\033[1;32mБуква \033[0;m{guess}\033[1;32m есть в слове!\033[0;m')
                for i in range(len_h):
                    if hid_word[i] == guess:
                        cur_word[i] = guess

                continue

            else:
                guess_player.append(guess)
                tries -= 1
                print(f'\n\033[1;31mБуквы \033[0;m{guess}\033[1;31m нет в слове.\033[0;m')
                continue

        else:  # Если введено слово
            if guess == ''.join(hid_word):
                print('\n\033[1;30;42mОтлично, Вы угадали слово!\033[0;0;m')
                status(hid_word, tr_base, tries)
                break

            else:
                guess_player.append(guess)
                tries -= 1
                print('\n\033[1;31mВведенное слово не является загаданным\033[0;m')
                continue

    if tries == 0:
        loose = ''.join(hid_word)
        print(f'\n\033[1;30;41mНе вышло. Загаданное слово: {loose}.\033[0;0;m')


def start():
    print('\nПриветствую Вас в Угадайке слов!\nОпределите нижеследующие настройки:')

    while True:
        t = 6
        req_1 = choose_yn(input('\nОткрыть первую и последнюю буквы? (Да / Нет) '))
        req_2 = choose_yn(input('\nСтандартное количество попыток 6.\n'
                                'Желаете изменить количество попыток? (Да / Нет) '))
        if req_2:
            t = input('\nВведите число попыток: ')
            while not t.isdigit() or int(t) < 1:
                t = input('\nВведите число, большее 1: ')
            t = int(t)

        game(req_1, t)  # Запуск игры

        if not choose_yn(input('\nЖелаете сыграть еще раз? (Да / Нет) ')):
            break

    print('\nЗавершение программы.')


start()
