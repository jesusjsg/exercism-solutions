"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature: float | int, neutrons_emitted: int) -> bool:
    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 5e5
    )


def reactor_efficiency(
    voltage: float | int, current: float | int, theorical_max_power: float | int
) -> str:
    generated_power = voltage * current
    efficiency = (generated_power / theorical_max_power) * 100

    if efficiency >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"
    return "black"


def fail_safe(
    temperature: float | int, neutrons_produced_per_second: int, threshold: float | int
) -> str:
    mid_temperature = temperature * neutrons_produced_per_second

    if mid_temperature < threshold * 0.9:
        return "LOW"
    if mid_temperature <= threshold * 1.1:
        return "NORMAL"
    return "DANGER"
