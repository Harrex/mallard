import sqlite3
from typing import List
import mallard


# Worth a read - Intro to SQL: https://learnsql.com/blog/sql-101/
# https://learnsql.com/blog/sql-basics-cheat-sheet/


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(mallard.DATABASE_FILE)
        self.cur = self.connection.cursor()

    def create_table(self, table_name: str, columns: List[str]):
        # Join function: https://pythonbasics.org/join/
        # F-strings https://realpython.com/python-string-formatting/#using-f-strings-to-format-strings

        # Create a new database table, or if it exists, just find that
        self.cur.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        )

    def add_to_table(self, table_name: str, columns: List[str], values: List):
        print(values)
        self.cur.execute(
            f""" INSERT INTO {table_name} ({', '.join(columns)}) 
            VALUES ({', '.join(["\'" + str(value) + "\'" for value in values])}) """
        )
