def settings():
    sett = list()
    sett.append(valid_txt(input('\n1. Произвести шифровку или дешифровку? (ш / д) '), 'drct'))  # T / F
    sett.append(valid_txt(input('\n2. Выберите язык (ru / en): '), 'lang'))  # T / F
    sett.append(valid_dig(input('\n3. Введите шаг сдвига: ')))  # сдвиг
    sett.append(input('\n4. Введите текст для преобразования: '))
    return sett


def valid_txt(req, opt):
    if opt == 'lang':
        while req not in ['ru', 'rus', 'r', 'en', 'eng', 'e']:
            req = input('Некорректное значение. Введите (ru / en): ')
        if req in ['ru', 'rus', 'r']:
            return True
        else:
            return False

    if opt == 'drct':
        while req not in ['ш', 'шифровка', 'i', 'д', 'дешифровка', 'l']:
            req = input('Некорректное значение. Введите (ш / д): ')
        if req in ['ш', 'шифровка', 'i']:
            return True
        else:
            return False


def valid_dig(req):
    while not req.isdigit():
        req = input('Некорректное значение. Введите число: ')
    return int(req)


def process(drct, lang, n, txt):
    # Шифровка = drct = True // Дешифровка = drct = False
    # lang = True = rus // lang = False = eng
    key, res = [], []
    key.extend('абвгдежзийклмнопрстуфхцчшщъыьэюя' * lang + 'abcdefghijklmnopqrstuvwxyz' * (not lang))
    mod_n = len(key)
    for i in range(len(txt)):
        if txt[i].isalpha() and txt[i].islower():  # Если буква строчная
            ind = (key.index(txt[i]) + n * drct - n * (not drct)) % mod_n
            res.append(key[ind])
        elif txt[i].isalpha() and txt[i].isupper():  # Если буква прописная
            ind = (key.index(txt[i].lower()) + n * drct - n * (not drct)) % mod_n
            res.append(key[ind].upper())
        else:  # для остальных символов
            res.append(txt[i])

    return res


def choose_yn(req):
    while req.lower() not in ["да", "нет", "lf", "ytn"]:
        req = input("Некорректный ответ. Введите (Да / Нет): ")
    if req.lower() in ["да", "lf"]:
        return True
    else:
        return False


def again():
    if choose_yn(input('\nЖелаете еще раз воспользоваться программой? (Да / Нет) ')):
        if choose_yn(input('\nОставить прежние настройки? (Да / Нет) ')):
            return 1
        else:
            return 2
    else:
        return False


def start():
    flag = True
    print('\nПрограмма для шифровки / дешифровки текста.\nОпределите нижеследующие настройки:')
    setts = settings()  # Сохранение настроек в список
    print('\nВывожу конвертированный текст:')
    print(*process(setts[0], setts[1], setts[2], setts[3]), sep='')

    while flag:
        ag = again()
        if ag == 1:  # С прежними настройками
            req = input('\nВведите текст для преобразования: ')
            print('\nВывожу конвертированный текст:')
            print(*process(setts[0], setts[1], setts[2], req), sep='')
        elif ag == 2:  # С новыми настройками
            setts = settings()
            print('\nВывожу конвертированный текст:')
            print(*process(setts[0], setts[1], setts[2], setts[3]), sep='')
        else:  # Выход из программы
            flag = False

    print('\nЗавершение программы.')


start()
