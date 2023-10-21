# Калькулятор системы счисления
def again():
    ag = input("\nЖелаете еще конвертировать число? (Да / Нет): ")
    while ag.lower() not in ["да", "нет", "lf", "ytn"]:
        ag = input("Некорректный ответ. Введите (Да / Нет): ")
    if ag.lower() in ["да", "lf"]:
        return True
    else:
        return False


def valid_base(base: str, base_ch: int):
    while not base.isdigit() or not (1 < int(base) < 37 and int(base) != base_ch):
        base = input('Некорректное значение.\nВведите число от 2 до 36' + f', исключая {base_ch}'
                     * (base == str(base_ch)) + ': ')

    return int(base)


def valid_num(base: int):
    flag = True
    simb = '0123456789ABCDEFGHIJKLMNPQRSTUYVWXYZ'  # Допустимые символы
    print('\n2. Введите исходное число: ', end='')
    while flag:
        n = input()
        flag = False
        for i in n:
            if i.upper() not in simb[:base]:
                flag = True
                print(f'\nНекорректное значение. Допустимые символы для основания {base}: "{simb[:base]}".')
                print('Введите число заново: ', end='')
                break

    return n


def to_dec(num: str, base: int):  # Перевод в 10-ую
    return int(num, base)


def to_base(num: str, base_old: int, base_new: int):  # Для всех, кроме 10-ой
    num = to_dec(num, base_old)
    res = ''
    while num:
        ost = num % base_new
        res = str(num % base_new) * (ost < 10) + chr(ord('A') - 10 + ost) * (ost > 9) + res
        num //= base_new

    return res


def settings():
    sett = list()
    sett.append(valid_base(input('\n1. Введите исходное основание: '), 0))
    sett.append(valid_num(sett[0]))
    sett.append(valid_base(input('\n3. Введите новое основание: '), sett[0]))

    return sett


def start():
    print('-' * 38, '\nЗапущен калькулятор системы счисления.\nОпределите следующие настройки:\n', '-' * 38, sep='')

    flag = True
    while flag:
        setts = settings()
        if setts[2] == 10:
            print(f'Число {setts[1].upper()} с основанием {setts[0]} конвертировано в число {to_dec(setts[1], setts[0])} с основанием {setts[0]}.')

        else:
            print(f'Число {setts[1].upper()} с основанием {setts[0]} конвертировано в число {to_base(setts[1], setts[0], setts[2])} с основанием {setts[2]}.')

        flag = again()

    print()
    print('-' * 38, '\nПрограмма завершена.\n', '-' * 38, sep='')


start()
