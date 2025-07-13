"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple) -> str:
    return record[1]


def convert_coordinate(coordinate: str) -> tuple:
    return tuple(coordinate)


def compare_records(azara_record: tuple, rui_record: tuple) -> bool:
    return convert_coordinate(azara_record[1]) == convert_coordinate(rui_record[1])


def create_record(azara_record: tuple, rui_record: tuple) -> tuple | str:
    if not compare_records(azara_record, rui_record):
        return "not a match"
    return azara_record + rui_record


def clean_up(combined_record: tuple) -> str:
    report = ""
    for record in combined_record:
        report += str(record[:1] + record[2:]) + "\n"
    return report


print(get_coordinate(("Azara", "1,1")))
print(convert_coordinate("11"))
print(compare_records(("Azara", "1,1"), ("Rui", "1,1")))
print(create_record(("Azara", "1,1"), ("Rui", "1,1")))
print(
    clean_up(
        (
            ("Brass Spyglass", "4B", "Abandoned Lighthouse", ("4", "B"), "Blue"),
            (
                "Vintage Pirate Hat",
                "7E",
                "Quiet Inlet (Island of Mystery)",
                ("7", "E"),
                "Orange",
            ),
            ("Crystal Crab", "6A", "Old Schooner", ("6", "A"), "Purple"),
        )
    )
)
