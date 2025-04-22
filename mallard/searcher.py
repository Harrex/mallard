from typing import Dict, List
from mallard.database import Database


class Searcher:

    # Split this into a separate class, so that we can change search queries
    # without constantly re-pulling data from the database - should speed
    # things up a bit.

    def __init__(self, database: Database):
        self.database = database

    def get_searchable_items(self, table_name: str, column: str) -> Dict[str, int]:
        """
        Return a dictionary of items in `column`, matched with the ID.
        """

        result = self.database.cur.execute(f"SELECT {column}, id FROM {table_name}")
        # Convert sql result to python list of tuples, then to a dictionary
        result = dict(result.fetchall())

        return result

    def value_search(self, table_name: str, column: str, query: str) -> List:
        """
        Get the
        """

        # We don't know necessarily what type of value this will return, so
        # don't specify (just use List instead of eg. List[str])

        # Create this empty list at the beginning. As we find valid results,
        # we'll add them to this list and return it at the end.
        return_values: List = []

        # Now for a search algorithm - We want 'fuzzy-finding':
        # - Case-insensitive
        # - Can search anywhere in a phrase

        # For case-insensitive, we can just convert everything to lowercase

        query = query.lower()

        # First, let's get the names, then convert to lowercase
        searchable = self.get_searchable_items(table_name, column)
        searchable_lower = {key.lower(): ID for (key, ID) in searchable.items()}

        # We just want to search up the list of values. Then, we can lookup the correct ID at the end
        searchable_lower_values: List[str] = [i for i in searchable_lower.keys()]

        # Do this in several passes - each one will permit more results
        # Later passes will usually be slower

        # Exact matches (case insensitive)
        # This can be done with a simple list filter
        # https://realpython.com/python-filter-function/
        # See also https://www.w3schools.com/python/python_lambda.asp

        exact_matches = filter(lambda x: x == query, searchable_lower_values)
        return_values += [match for match in exact_matches]

        # Contains
        # Now look for anything that contains the query
        contains_matches = filter(lambda x: query in x, searchable_lower_values)
        return_values += [match for match in contains_matches]

        return return_values

    def id_search(self, table_name: str, column: str, query: str) -> List[int]:
        # Here, we can just call value_search, then lookup each ID.
        searchable = self.get_searchable_items(table_name, column)
        searchable_lower = {key.lower(): ID for (key, ID) in searchable.items()}

        values = self.value_search(table_name, column, query)
        ids = [searchable_lower[key] for key in values]

        return ids
