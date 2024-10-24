import random
import time

# "Ближайшее число" 
# В этой игре программа генерирует случайное число, и два игрока (компьютер и пользователь) пытаются угадать, кто из них окажется ближе к загаданному числу.

# Функция для броска случайного числа игроком (компьютером или пользователем)
def make_guess(player):
    if player == "компьютер":
        guess = random.randint(1, 100)  # Компьютер делает случайную попытку
        print(f"{player} выбрал число: {guess}")
    else:
        guess = int(input(f"{player}, введите число от 1 до 100: "))  # Пользователь вводит число
    return guess


# Функция для вычисления победителя на основе ближайшего числа к загаданному
def find_winner(secret_num, comp_guess, user_guess):
    comp_diff = abs(secret_num - comp_guess)  # Разница между загаданным числом и выбором компьютера
    user_diff = abs(secret_num - user_guess)  # Разница между загаданным числом и выбором пользователя

    print(f"Загаданное число было: {secret_num}")

    if comp_diff < user_diff:
        print("Компьютер ближе к загаданному числу! Он победил!")
    elif user_diff < comp_diff:
        print("Вы ближе к загаданному числу! Вы победили!")
    else:
        print("Оба игрока выбрали числа одинаково близко! Ничья!")


# Основная функция игры
def play_closest_number_game():
    print("Добро пожаловать в игру 'Ближайшее число'!")
    secret_num = random.randint(1, 100)  # Программа загадывает число от 1 до 100
    time.sleep(1)
    print("Программа загадала число от 1 до 100.\n")

    # Компьютер делает попытку
    comp_guess = make_guess("компьютер")

    # Пользователь делает попытку
    user_guess = make_guess("Пользователь")

    # Определяем победителя
    find_winner(secret_num, comp_guess, user_guess)


# Запуск игры
play_closest_number_game()
