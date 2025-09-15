"""Functions to manage a users shopping cart items."""

from typing import Iterable


def add_item(current_cart: dict, items_to_add: list) -> dict:
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart


def read_notes(notes: list | tuple) -> dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = dict.fromkeys(notes, 1)
    return cart


def update_recipes(ideas: dict, recipe_updates: Iterable) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: dict):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    pass


print(add_item({"egg": 1, "milk": 1}, ["egg", "milk", "egg"]))
print(read_notes(["egg", "milk", "egg"]))
print(
    update_recipes(
        {
            "Banana Bread": {
                "Banana": 1,
                "Apple": 1,
                "Walnuts": 1,
                "Flour": 1,
                "Eggs": 2,
                "Butter": 1,
            },
            "Raspberry Pie": {
                "Raspberry": 1,
                "Orange": 1,
                "Pie Crust": 1,
                "Cream Custard": 1,
            },
        },
        (
            (
                "Banana Bread",
                {
                    "Banana": 4,
                    "Walnuts": 2,
                    "Flour": 1,
                    "Butter": 1,
                    "Milk": 2,
                    "Eggs": 3,
                },
            ),
        ),
    )
)
print(sort_entries({"egg": 1, "milk": 1, "apple": 1}))
