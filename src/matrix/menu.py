from typing import Callable

LOOP = 0
UP = 1
EXIT = 2
PROMPT = 'Your choice: '


class Menu:
    def __init__(self, text: str, menu_actions: dict[str, Callable[[], int]], invalid_message: str = 'Invalid input\n'):
        self.text = text
        self.menu_actions = menu_actions
        self.invalid_message = invalid_message

    def run_once(self) -> int:
        print(self.text)
        choice = input(PROMPT)
        while choice not in self.menu_actions:
            print(self.invalid_message)
            choice = input(PROMPT)
        return self.menu_actions[choice]()

    def loop(self) -> int:
        status = self.run_once()
        while status == LOOP:
            status = self.run_once()
        return EXIT if status == EXIT else status - 1
