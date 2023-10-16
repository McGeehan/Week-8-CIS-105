def get_average(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)  # Fixed Bug 1
    return average

scores = [90, 80, 70, 60, 50]
print("The average score is: ", get_average(scores))  # Fixed Bug 2
