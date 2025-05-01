from dataclasses import dataclass


# Dataclasses automatically generate the init method - they look a bit cleaner
# for simply representing data
# https://docs.python.org/3/library/dataclasses.html
@dataclass
class Address:
    line_1: str
    line_2: str
    city: str
    state: str
    post_code: str

    # Associations - Potentially change to enumerators later
    # https://docs.python.org/3/library/enum.html
    territory: str
    market_segment: str

    def __str__(self):
        return f"""
{ self.line_1 }
{ self.line_2 }
{ self.city }
{ self.state }
{ self.post_code }    
    """
