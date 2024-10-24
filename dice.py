from random import randint
from time import sleep

# Функция для отображения кубика в виде текста
def print_dice(roll):
    dice = {
        1: ("[     ]",
            "[  o  ]",
            "[     ]"),
        2: ("[o    ]",
            "[     ]",
            "[    o]"),
        3: ("[o    ]",
            "[  o  ]",
            "[    o]"),
        4: ("[o   o]",
            "[     ]",
            "[o   o]"),
        5: ("[o   o]",
            "[  o  ]",
            "[o   o]"),
        6: ("[o   o]",
            "[o   o]",
            "[o   o]")
    }

    for line in dice[roll]:
        print(line)

# Бросок кубика
def roll_dice():
    print("Бросаем кубик...")
    sleep(1)  # Добавляем паузу для реалистичности
    roll = randint(1, 6)
    print(f"Выпало число: {roll}")
    print_dice(roll)  # Отображаем кубик
    return roll

# Запуск программы
roll_dice()
