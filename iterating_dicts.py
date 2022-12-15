test_scores = {
    "Alan": 100,
    "Alex": 98,
    "Leandro": 97,
    "Robert": 96,
    "Renan": 85,
    "Marsha": 78,
    "Baker": 69,
    "Rosa": 92,
    "Leif": 97,
    "Peng": 61,
    "Juan": 73,
    "Esteban": 84,
    "Amir": 91,
    "Sakura": 99
}

# iterate to find dicts keys using key()
for student in test_scores.keys():
    print(student)

# iterate to find dicts values using values()
for score in test_scores.values():
    print(score)

# iterate to find the average of dicts values using values()
total = 0
for score in test_scores.values():
    total += score
print(total/len(test_scores))

# iterate to find dicts keys and plug values to keys using keys()
for key in test_scores.keys():
    print(key, test_scores[key])

# iterate to find dicts keys and values using items()
for item in test_scores.items():
    print(item)

# iterate to unpack the dicts keys and values using items()
for key, value in test_scores.items():
    print(key, value)

# iterate to find out who had the highest test score in dicts keys and values using items()
max_score = 0
best_student = ""
for student, score in test_scores.items():
    if score > max_score:
        max_score = score
        best_student = student
print(f"Highest score was {max_score} by {best_student}")