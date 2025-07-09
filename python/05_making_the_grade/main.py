"""Functions for organizing and calculating student exam scores."""


def round_scores(scores: list) -> list:
    return [round(score) for score in scores]


def count_failed_students(scores: list) -> int:
    return sum(1 for score in scores if score <= 40)


def above_threshold(student_scores: list, threshold: int) -> list:
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list:
    interval = round((highest - 40) / 4)
    return [41 + interval * index for index in range(4)]


def student_ranking(student_scores: list, student_names: list) -> list:
    ranking = []
    for index, name in enumerate(student_names):
        ranking.append(f"{index + 1}. {name}: {student_scores[index]}")
    return ranking


def perfect_score(student_info: list) -> list:
    for student in student_info:
        name, score = student
        if score == 100:
            return [name, score]
    return []


print(round_scores([0.5, 0.3, 0.7, 0.2, 0.1]))
print(count_failed_students([80, 70, 60, 50, 40]))
print(above_threshold([80, 70, 60, 50, 40], 60))
print(letter_grades(100))
print(student_ranking([80, 70, 60, 50, 40], ["A", "B", "C", "D", "E"]))
print(perfect_score([["A", 100], ["B", 100], ["C", 80], ["D", 70], ["E", 60]]))
