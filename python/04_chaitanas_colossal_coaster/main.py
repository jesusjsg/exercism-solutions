"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(
    express_queue: list, normal_queue: list, ticket_type: int, person_name: str
) -> list:
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: list, friend_name: str) -> int:
    return queue.index(friend_name)


def add_me_to_with_my_friends(queue: list, index: int, friend_name: str) -> list:
    queue.insert(index, friend_name)
    return queue


def remove_the_mean_person(queue: list, person_name: str) -> list:
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list, person_name: str) -> int:
    return queue.count(person_name)


def remove_the_last_person(queue: list) -> str:
    return queue.pop()


def sorted_names(queue: list) -> list:
    return sorted(queue)


print(add_me_to_the_queue(["Express"], ["Normal"], 0, "John"))
print(find_my_friend(["Sort", "Bito"], "Sort"))
print(add_me_to_with_my_friends(["Sort", "Bito"], 1, "Sort"))
print(remove_the_mean_person(["Sort", "Bito"], "Sort"))
print(how_many_namefellows(["Sort", "Bito"], "Sort"))
print(remove_the_last_person(["Sort", "Bito"]))
print(sorted_names(["Sort", "Bito"]))
