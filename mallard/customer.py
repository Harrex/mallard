import mallard
import time
from typing import List
from mallard.order import Order
from mallard.address import Address


class Customer:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        address: Address,
    ):
        # I'm using vaguely google-style docstrings here. It doesn't really
        # matter but consistency within a project is nice
        #
        # https://www.geeksforgeeks.org/python-docstrings/
        # https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings
        """
        Creates a new customer given all necessary details. Generates an ID
        from the unix timestamp, and an empty list of orders

        Args:
            first_name (str) : The customer's first name
            last_name (str) : The customer's last name
            email (str) : The customer's email
            phone_number (int) : The customer's phone number
            address (Address) : The customer's address, using the `Address` dataclass
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.orders = []

        # Generate an ID from the Unix timestamp
        # TODO: improve this method (probably use hash)
        self.id = int(time.time() * 100) % 1000000

    def __str__(self):
        return f"""
        { self.first_name } { self.last_name }
        { self.email }, { self.phone_number }
        { self.address }
              """
