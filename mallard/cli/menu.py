from typing import List

# A class for menus.


class Menu:
    def __init__(self, options: List[str]):
        self.options = options

    def choose(self) -> str:
        """
        Prints out the options to the screen along with an input for the user to select one.
        Returns:
            (str) - The item that the user selected
        """

        # Let's start from one here to make this more user friendly. Note that
        # we'll have to subtract 1 from the user's choice later to compensate,
        # because computers count from 0

        i = 1
        # First, loop through and print out the options, with a
        # number for the user to select
        for option in self.options:
            print(f"({i})  {option}")
            i += 1

        user_choice = int(input("Please select an option: "))
        return self.options[user_choice - 1]
