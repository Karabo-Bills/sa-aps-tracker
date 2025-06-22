def calculate_aps(subjects_with_marks):
    aps = 0
    for subject, mark in subjects_with_marks.items():
        if mark >= 80:
            aps += 7
        elif mark >= 70:
            aps += 6
        elif mark >= 60:
            aps += 5
        elif mark >= 50:
            aps += 4
        elif mark >= 40:
            aps += 3
        elif mark >= 30:
            aps += 2
        else:
            aps += 1
    return aps
