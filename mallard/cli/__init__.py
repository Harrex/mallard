# This is a submodule. It will contain the UI components for
# mallard to be used in the command line interface.

import os, sys

from mallard.address import Address
from mallard.customer import Customer
from mallard.cli.form import Form
from mallard.cli.menu import Menu
from mallard.database import Database


class CLI:

    def __init__(self):
        ## Currently, our init method doesn't need to do anything special.
        pass

    # This is our main function - the entry point for the tui
    def run(self):

        database = Database()
        # Clear the console. Note that on Linux and Darwin (MacOS), the
        # command is clear, while on Windows it's cls. Supporting
        # Windows isn't in scope at the moment because of things like
        # this.
        os.system("clear")
        print(f"Mallard CLI running on {sys.platform}")

        # Now, we want to enter the main program loop (i.e. the main menu)
        # Here, the user will choose an option, and the appropriate function
        # will run.

        main_menu = Menu(
            options=["Add new Customer", "Search", "Save changes to Database", "Exit"]
        )
        while True:  # Loop this forever
            os.system("clear")
            choice = main_menu.choose()
            match choice:
                case "Add new Customer":
                    # first_name: str,
                    # last_name: str,
                    # email: str,
                    # phone_number: int,
                    # address: Address,
                    customer_form = Form(
                        ["First Name", "Last Name", "Email", "Phone Number"],
                        "Customer Information",
                    )
                    customer_responses = customer_form.get_responses()
                    address_form = Form(
                        [
                            "Line 1",
                            "Line 2",
                            "City",
                            "State",
                            "Post Code",
                            "Territory",
                            "Market Segment",
                        ],
                        "Address Information",
                    )
                    address_responses = address_form.get_responses()

                    # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
                    customer_addr = Address(*address_responses)
                    new_customer = Customer(
                        *(customer_responses),
                        address=customer_addr,
                    )

                    print(new_customer)
                    input("OK? (y/n) ")

                    # TODO: Add the customer to the database
                    # database.add_to_table("Customers")

                case "Search":
                    print("Not implemented")
                case "Save changes to Database":
                    print("Not implemented")
                case "Exit":
                    exit()
