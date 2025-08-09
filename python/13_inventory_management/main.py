"""Functions to keep track and alter inventory."""


def create_inventory(items: list) -> dict:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def add_items(inventory: dict, items: list) -> dict:
    counts = create_inventory(items)
    for item, count in counts.items():
        inventory[item] = inventory.setdefault(item, 0) + count
    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory: dict) -> list:
    return [(item, count) for item, count in inventory.items() if count > 0]
