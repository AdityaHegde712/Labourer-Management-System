"""
Functions that don't directly interact with DB
But reduce burden on front-end logic.

Incomplete?
"""

from functools import reduce


def calculate_wage_by_phone_no(entries: list[dict], phone_no: str | None = None) -> int:
    """
    Pass dictionary list which is filtered by date range for utility.

    phone_no is optional\n
    If no phone_no is specified, function acts like a total expense
    calculator.
    """

    entries = list(
        filter(lambda entry: entry['phone_no'] == phone_no, entries)) if not phone_no == None else entries
    total_wage = reduce(lambda total_wage,
                        entry: total_wage + entry['wage'], entries, 0)

    return total_wage


# print(calculate_wage_by_phone_no(
#     [{'id': 1, 'name': 'Harsh M', 'phone_no': '8689905873',
#         'task': 'crawling', 'wage': 500, 'date': '2023-05-09'},
#         {
#             'phone_no': '99043434',
#             'wage': 433
#     }]))
