# Работа с файлами и директориями через os

import os

# Функция для вывода текущей директории
def print_current_directory():
    current_dir = os.getcwd()  # Получаем текущую директорию
    print(f"Текущая директория: {current_dir}")

# Функция для создания новой папки
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)  # Создаем новую директорию
        print(f"Папка '{directory_name}' успешно создана.")
    except FileExistsError:
        print(f"Папка '{directory_name}' уже существует.")
    except Exception as e:
        print(f"Ошибка при создании папки: {e}")

# Функция для удаления папки
def remove_directory(directory_name):
    try:
        os.rmdir(directory_name)  # Удаляем директорию
        print(f"Папка '{directory_name}' успешно удалена.")
    except FileNotFoundError:
        print(f"Папка '{directory_name}' не найдена.")
    except OSError:
        print(f"Папка '{directory_name}' не может быть удалена (возможно, она не пуста).")
    except Exception as e:
        print(f"Ошибка при удалении папки: {e}")

# Функция для вывода списка файлов и папок в текущей директории
def list_directory_contents():
    print("Содержимое текущей директории:")
    contents = os.listdir()  # Получаем список файлов и папок
    for item in contents:
        print(item)

# Основная логика программы
def main():
    while True:
        print("\nМеню:")
        print("1. Показать текущую директорию")
        print("2. Создать новую папку")
        print("3. Удалить папку")
        print("4. Показать содержимое текущей директории")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            print_current_directory()
        elif choice == "2":
            directory_name = input("Введите название новой папки: ")
            create_directory(directory_name)
        elif choice == "3":
            directory_name = input("Введите название папки для удаления: ")
            remove_directory(directory_name)
        elif choice == "4":
            list_directory_contents()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
