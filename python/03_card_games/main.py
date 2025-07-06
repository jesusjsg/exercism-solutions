"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list:
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    return rounds_1 + rounds_2


def list_contains_round(rounds: list, number: int) -> bool:
    """
    This solution is not very efficient, but it is a good example of how
    to loop through a list.
    You can use the `in` operator to check if a number is in a list.

    return number in rounds
    """

    for round in rounds:
        if round == number:
            return True
    return False


def card_average(hand: list) -> float:
    # return sum(hand) / len(hand)
    value = 0
    for card in hand:
        value += card
    return value / len(hand)


def approx_average_is_average(hand: list) -> bool:
    first = hand[0]
    last = hand[-1]
    middle = hand[len(hand) // 2]

    actual_average = card_average(hand)
    average_first_last = card_average([first, last])
    return actual_average in (average_first_last, middle)


def average_even_is_average_odd(hand: list) -> bool:
    return card_average(hand) == card_average(hand[1::2])


def maybe_double_last(hand: list) -> list:
    if hand[-1] == 11:
        return hand[:-1] + [22]
    return hand


print(get_rounds(2))
print(concatenate_rounds([1, 2, 3], [4, 5, 6]))
print(card_average([5, 6, 7]))
print(approx_average_is_average([1, 2, 3, 5, 9]))
print(average_even_is_average_odd([1, 2, 3, 4]))
print(maybe_double_last([1, 2, 11]))
