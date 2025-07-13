EXPECTED_BAKE_TIME = 40


def bake_time_remaining(cook: int) -> int:
    return EXPECTED_BAKE_TIME - cook


def preparation_time_in_minutes(layers: int) -> int:
    return layers * 2


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
