def grades(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    elif grade <= 3.49:
        return "Poor"
    elif grade <= 4.49:
        return "Good"
    elif grade <= 5.49:
        return "Very Good"
    elif grade <= 6:
        return "Excellent"


grade = float(input())
print(grades(grade))
