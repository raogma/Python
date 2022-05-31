def is_fail(grade):
    return 2 <= grade <= 2.99


def is_poor(grade):
    return 3 <= grade <= 3.49


def is_good(grade):
    return 3.5 <= grade <= 4.49


def is_very_good(grade):
    return 4.5 <= grade <= 5.49


def is_excellent(grade):
    return 5.5 <= grade <= 6
