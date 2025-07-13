def exchange_money(budget: float, exchange_rate: float) -> float:
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> float:
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    return int(amount / denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    return amount % denomination


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    ex_budget = exchange_money(budget, (exchange_rate + (exchange_rate * spread / 100)))
    return int(get_change(ex_budget, get_leftover_of_bills(ex_budget, denomination)))


print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))
