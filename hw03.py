
import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)


def print_directory(path, indent=""):
    """
    Рекурсивно виводить структуру директорії.
    Директорії відображаються синім кольором,
    файли — зеленим.
    """

    # Отримуємо список елементів директорії
    items = sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))

    for index, item in enumerate(items):

        # Визначаємо, чи є елемент останнім
        is_last = index == len(items) - 1

        # Формуємо символи дерева
        branch = "┗ " if is_last else "┣ "

        if item.is_dir():
            # Виводимо назву директорії синім кольором
            print(indent + branch + Fore.BLUE + item.name + "/")

            # Формуємо відступ для наступного рівня
            new_indent = indent + ("  " if is_last else "┃ ")

            # Рекурсивно обходимо піддиректорію
            print_directory(item, new_indent)

        else:
            # Виводимо назву файлу зеленим кольором
            print(indent + branch + Fore.GREEN + item.name)


def main():
    # Перевіряємо наявність аргументу командного рядка
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        return

    # Отримуємо шлях до директорії
    directory_path = Path(sys.argv[1])

    # Перевіряємо існування шляху
    if not directory_path.exists():
        print(f"Помилка: шлях '{directory_path}' не існує.")
        return

    # Перевіряємо, чи є шлях директорією
    if not directory_path.is_dir():
        print(f"Помилка: '{directory_path}' не є директорією.")
        return

    # Виводимо кореневу директорію
    print(Fore.BLUE + f"📦 {directory_path.name}")

    # Виводимо структуру директорії
    print_directory(directory_path)


if __name__ == "__main__":
    main()
