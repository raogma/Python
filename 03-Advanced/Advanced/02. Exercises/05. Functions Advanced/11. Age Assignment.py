def age_assignment(*args, **kwargs):
    data = {name: 0 for name in args}
    for first_letter in kwargs:
        for key in data:
            if first_letter in key:
                data[key] = kwargs[first_letter]
    return data


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

