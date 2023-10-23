# Калькулятор системы счисления
def ask_user_to_work_again():
    again = input("\nЖелаете еще конвертировать число? (Да / Нет): ")
    while again.lower() not in ["да", "нет", "lf", "ytn"]:
        again = input("Некорректный ответ. Введите (Да / Нет): ")
    if again.lower() in ["да", "lf"]:
        return True
    else:
        return False


def is_base_valid(base: str, base_old: int):
    while not base.isdigit() or not (1 < int(base) < 37 and int(base) != base_old):
        base = input(
            "Некорректное значение.\nВведите число от 2 до 36"
            + f", исключая {base_old}" * (base == str(base_old))
            + ": "
        )

    return int(base)


def is_num_valid(base: int):
    flag = True
    symbols = "0123456789ABCDEFGHIJKLMNPQRSTUYVWXYZ"  # Допустимые символы
    print("\n2. Введите исходное число: ", end="")
    while flag:
        num = input()
        flag = False
        for i in num:
            if i.upper() not in symbols[:base]:
                flag = True
                print(
                    f'\nНекорректное значение. Допустимые символы для основания {base}: "{symbols[:base]}".'
                )
                print("Введите число заново: ", end="")
                break

    return num


def to_decimal(num: str, base: int):  # Перевод в 10-ую
    return int(num, base)


def to_base(num: str, base_old: int, base_new: int):  # Для всех, кроме 10-ой
    num = to_decimal(num, base_old)
    result = ""
    while num:
        remainder = num % base_new
        result = (
            str(num % base_new) * (remainder < 10)
            + chr(ord("A") - 10 + remainder) * (remainder > 9)
            + result
        )
        num //= base_new

    return result


def get_user_settings(): 
    settings = list()
    settings.append(is_base_valid(input("\n1. Введите исходное основание: "), 0))
    settings.append(is_num_valid(settings[0]))
    settings.append(is_base_valid(input("\n3. Введите новое основание: "), settings[0]))

    return settings


def main():
    print(
        "-" * 38,
        "\nЗапущен калькулятор системы счисления.\nОпределите следующие настройки:\n",
        "-" * 38,
        sep="",
    )

    flag = True
    while flag:
        settings = get_user_settings()
        if settings[2] == 10:
            print(
                f"Число {settings[1].upper()} с основанием {settings[0]} конвертировано в число {to_decimal(settings[1], settings[0])} с основанием {settings[0]}."
            )

        else:
            print(
                f"Число {settings[1].upper()} с основанием {settings[0]} конвертировано в число {to_base(settings[1], settings[0], settings[2])} с основанием {settings[2]}."
            )

        flag = ask_user_to_work_again()

    print()
    print("-" * 38, "\nПрограмма завершена.\n", "-" * 38, sep="")


main()
