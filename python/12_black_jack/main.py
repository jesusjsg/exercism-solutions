"""Functions to help play and score a game of blackjack."""


def value_of_card(card: str) -> int:
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str) -> tuple | str:
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    if card_one == "A" and card_two == "A":
        return 1
    return 11 if (value_of_card(card_one) + value_of_card(card_two) <= 10) else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    return (card_one == "A" and value_of_card(card_two) == 10) or (
        card_two == "A" and value_of_card(card_one) == 10
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    result = value_of_card(card_one) + value_of_card(card_two)
    if result in [0, 10, 11]:
        return True
    return False
