# Магический шар
from random import *
from time import *


def rand_answer():
    question = input("Введите, пожалуйста, свой вопрос: ")
    sleep(1)
    answer = [
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо да",
        "Можешь быть уверен в этом",
        "Мне кажется - да",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят - да",
        "Да",
        "Пока неясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять",
        "Даже не думай",
        "Нет",
        "По моим данным - нет",
        "Перспективы не очень хорошие",
        "Весьма сомнительно",
    ]
    print("Хорошо, дайте подумать...\n")
    sleep(1)
    return choice(answer)


def greets():
    print("Приветствую! С Вами разговаривает эмуляция волшебного шара!")
    sleep(0.5)
    name = input("Как я могу к Вам обращаться?\n" "Введите имя: ")
    return name


def game():
    player_name = greets()
    print(f"Рад знакомству, {player_name}!")
    print(rand_answer())
    flag = ask_user_to_play_again()
    while flag:
        print(rand_answer())
        flag = ask_user_to_play_again()

    sleep(1)
    print(f"Спасибо тебе, {player_name}, что обратился! Приходи еще!")


def ask_user_to_play_again():
    ask = input("\nЖелаете задать новый вопрос? (Да / Нет): ")
    while ask.lower() not in ["да", "нет", "lf", "ytn"]:
        ask = input("Некорректный ответ. Введите (Да / Нет): ")
    if ask.lower() in ["да", "lf"]:
        return True
    else:
        return False


game()
