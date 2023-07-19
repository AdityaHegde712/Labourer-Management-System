"""
Functions that don't directly interact with DB
But reduce burden on front-end logic.

Incomplete?
"""


from functools import reduce


def calculate_wage(list_of_entries: list[dict]) -> int:
    """
    Pass list from any select statement
    """
    total_wage = reduce(lambda total_wage,
                        entry: total_wage + entry['wage'], list_of_entries, 0)

    return total_wage
