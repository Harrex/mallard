from typing import List


class Form:
    def __init__(self, fields: List[str], title=None):
        self.fields = fields
        self.num_fields = len(fields)
        self.title = title

    def get_responses(self) -> List[str]:
        """
        Prints out the fields to the screen along with an input for the user to
        fill each in. Returns the responses as a list.
        Returns:
            ([str]) - The user's responses
        """

        # Let's start from one here to make this more user friendly. Note that
        # we'll have to subtract 1 from the user's choice later to compensate,
        # because computers count from 0

        print(self.title)

        responses = []
        i = 1
        # First, loop through and print out the fields, with a
        # number for the user to select
        for field in self.fields:
            print(f"({i} / {self.num_fields})  {field}", end="")
            responses.append(input(": "))
            i += 1

        return responses
