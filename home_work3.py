import sys
from pathlib import Path
from colorama import Fore, Style, init

# Функція visualize_directory приймає шлях до директорії та виводить її вміст у вигляді дерева.
def visualize_directory(path, level=0):
    if not path.exists():
        print(f"Шлях {path} не існує.")
        return
    if path.is_dir():
        print(f"{'  '*level}{Fore.BLUE}{path.name}{Style.RESET_ALL}/")
        for item in path.iterdir():
            visualize_directory(item, level + 1)
    else:
        print(f"{'  '*level}{Fore.GREEN}{path.name}{Style.RESET_ALL}")

# Функція init() ініціалізує модуль colorama.
if __name__ == "__main__":
    init()
    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/вашої/директорії")
    else:
        dir_path = Path(sys.argv[1])
        visualize_directory(dir_path)





