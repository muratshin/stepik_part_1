def get_user_settings():
    settings = list()
    settings.append(
        is_text_valid(
            input("\n1. Произвести шифровку или дешифровку? (ш / д) "), "direct"
        )
    )
    settings.append(is_text_valid(input("\n2. Выберите язык (ru / en): "), "language"))
    settings.append(is_digit_valid(input("\n3. Введите шаг сдвига: ")))
    settings.append(input("\n4. Введите текст для преобразования: "))
    return settings


def is_text_valid(request, option):
    if option == "language":
        while request not in ["ru", "rus", "r", "en", "eng", "e"]:
            request = input("Некорректное значение. Введите (ru / en): ")
        if request in ["ru", "rus", "r"]:
            return True
        else:
            return False

    if option == "direct":
        while request not in ["ш", "шифровка", "i", "д", "дешифровка", "l"]:
            request = input("Некорректное значение. Введите (ш / д): ")
        if request in ["ш", "шифровка", "i"]:
            return True
        else:
            return False


def is_digit_valid(request):
    while not request.isdigit():
        request = input("Некорректное значение. Введите число: ")
    return int(request)


def start_encryption(direct: bool, language: bool, shift: int, txt: str):
    # Шифровка = drct = True // Дешифровка = drct = False
    # lang = True = rus // lang = False = eng
    key, res = [], []
    key.extend(
        "абвгдежзийклмнопрстуфхцчшщъыьэюя" * language
        + "abcdefghijklmnopqrstuvwxyz" * (not language)
    )
    mod_n = len(key)
    for i in range(len(txt)):
        if txt[i].isalpha() and txt[i].islower():  # Если буква строчная
            ind = (key.index(txt[i]) + shift * direct - shift * (not direct)) % mod_n
            res.append(key[ind])
        elif txt[i].isalpha() and txt[i].isupper():  # Если буква прописная
            ind = (
                key.index(txt[i].lower()) + shift * direct - shift * (not direct)
            ) % mod_n
            res.append(key[ind].upper())
        else:  # для остальных символов
            res.append(txt[i])

    return res


def ask_user_yes_no(request):
    while request.lower() not in ["да", "нет", "lf", "ytn"]:
        request = input("Некорректный ответ. Введите (Да / Нет): ")
    if request.lower() in ["да", "lf"]:
        return True
    else:
        return False


def ask_user_to_work_again():
    if ask_user_yes_no(
        input("\nЖелаете еще раз воспользоваться программой? (Да / Нет) ")
    ):
        if ask_user_yes_no(input("\nОставить прежние настройки? (Да / Нет) ")):
            return 1
        else:
            return 2
    else:
        return False


def start():
    flag = True
    print(
        "\n"
        "Программа для шифровки / дешифровки текста.\n"
        "Определите нижеследующие настройки:"
    )
    settings = get_user_settings()  # Сохранение настроек в список
    print("\nВывожу конвертированный текст:")
    print(*start_encryption(settings[0], settings[1], settings[2], settings[3]), sep="")

    while flag:
        again = ask_user_to_work_again()
        if again == 1:  # С прежними настройками
            req = input("\nВведите текст для преобразования: ")
            print("\nВывожу конвертированный текст:")
            print(*start_encryption(settings[0], settings[1], settings[2], req), sep="")
        elif again == 2:  # С новыми настройками
            settings = get_user_settings()
            print("\nВывожу конвертированный текст:")
            print(
                *start_encryption(settings[0], settings[1], settings[2], settings[3]),
                sep=""
            )
        else:  # Выход из программы
            flag = False

    print("\nЗавершение программы.")


start()
