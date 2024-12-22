import os
import sys
import subprocess
import platform
import logging
color_code = {
    "purple": "\u001b[35m"
}
purple = color_code["purple"]
"""Устанавливает необходимые пакеты"""
Katrin_packages = [
    'pystyle',
    'pyfiglet',
    'marshal',
    'binascii',
    'random',
    'zlib',
    'base64',
    're',
    'os',
    'sys',
]
sbanner = """
███████╗██╗    ██╗██╗  ██╗██╗   ██╗██████╗ ██╗  ██╗
██╔════╝██║    ██║██║ ██╔╝██║   ██║██╔══██╗╚██╗██╔╝
███████╗██║ █╗ ██║█████╔╝ ██║   ██║██████╔╝ ╚███╔╝
╚════██║██║███╗██║██╔═██╗ ╚██╗ ██╔╝██╔══██╗ ██╔██╗
███████║╚███╔███╔╝██║  ██╗ ╚████╔╝ ██║  ██║██╔╝ ██╗
╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝

██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
"""
def display_banner():
    print(f'{color_code["purple"]}{sbanner}')
    def create_menu_section(title, items):
        """Создает секцию меню с заголовком и пунктами"""
        width = 37  # Фиксированная ширина для всех строк
        section = [f"┃ {title:<{width - 4}} ┃"]
        for item in items:
            section.append(f"┃    {item:<{width - 7}} ┃")
        return section

    # Определяем секции меню
    sections = {
        "": [
            "1: Как установить на wsl",
            "2: Установить на windows",
             " или termux",
            "0: Выйти",
            ""
        ],
    }
    width = 37  # Фиксированная ширина
    border = "━" * (width - 2)
    empty_line = f"┃{' ' * (width - 2)}┃"
    banner = [f"┏{border}┓"]
    for title, items in sections.items():
        banner.extend(create_menu_section(title, items))
    banner.append(f"┗{border}┛")
    for line in banner:
        print(line)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def Katrin_system_python():
    for package in Katrin_packages:
        try:
            #subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "--break-system-packages"])
            # Проверяем, установлен ли пакет
            __import__(package.replace('-', '_'))
            print(f'Пакет {package} уже установлен')
        except ImportError:
            print(f'Устанавливаем пакет {package}...')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--break-system-packages"])
                print(f'Пакет {package} успешно установлен')
            except subprocess.CalledProcessError as e:
                print(f'Ошибка при установке пакета {package}: {e}')
                logging.error(f'Ошибка при установке пакета {package}: {e}')

                # Специальная обработка для wmi (только для Windows)
    if platform.system() == 'Windows':
        try:
            import wmi
        except ImportError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--break-system-packages"])
                subprocess.check_call([sys.executable, "-m", "pip", "install", "wmi", "--break-system-packages"])
                print('Пакет wmi успешно установлен')
            except subprocess.CalledProcessError as e:
                print(f'Ошибка при установке пакета wmi: {e}')


def Katrin_not_system_python():
    for package in Katrin_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            # Проверяем, установлен ли пакет
            __import__(package.replace('-', '_'))
            print(f'Пакет {package} уже установлен')
        except ImportError:
            print(f'Устанавливаем пакет {package}...')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f'Пакет {package} успешно установлен')
            except subprocess.CalledProcessError as e:
                print(f'Ошибка при установке пакета {package}: {e}')
                logging.error(f'Ошибка при установке пакета {package}: {e}')

                # Специальная обработка для wmi (только для Windows)
    if platform.system() == 'Windows':
        try:
            import wmi
        except ImportError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                subprocess.check_call([sys.executable, "-m", "pip", "install", "wmi"])
                print('Пакет wmi успешно установлен')
            except subprocess.CalledProcessError as e:
                print(f'Ошибка при установке пакета wmi: {e}')
def main():
    clear_terminal()
    while True:
        display_banner()
        choice = int(input("Выбор: "))
        if choice == 0:
            clear_terminal()
            exit()
        if choice == 1:
            print(""" 
https://youtu.be/U8Su48wTqFk 
""")
            input("Нажмите Enter для продолжения...")
        elif choice == 2:
            print("1: Python был установлен в системе")
            print("2: Python установили вы")
            ch = int(input("Выбор: "))
            if ch == 1:
                print("Устанавливаем необходимые пакеты...")
                Katrin_system_python()
                print("Пакеты установлены")
                input("Нажмите Enter для продолжения...")
                subprocess.check_call([sys.executable, "katerine.py"])
            elif ch == 2:
                print("Устанавливаем необходимые пакеты...")
                Katrin_not_system_python()
                print("Пакеты установлены")
                input("Нажмите Enter для продолжения...")
                subprocess.check_call([sys.executable, "katerine.py"])


if __name__ == "__main__":
    main()
