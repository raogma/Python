class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validate_name(txt):
    name, domain = txt.split('@')
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")


def validate_at(txt):
    if '@' not in txt:
        raise MustContainAtSymbolError("Email must contain @")


def validate_domain(txt, iterable):
    for element in iterable:
        if txt[-4: len(txt)] == element or txt[-3: len(txt)] == element:
            return
    raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


domains = ['.com', '.bg', '.org', '.net']
while True:
    command = input()
    if command == 'End':
        break
    email = command

    validate_at(email)
    validate_name(email)
    validate_domain(email, domains)