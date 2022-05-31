from re import match


class EmailValidator:
    def __init__(self, min_length, mails: list, domains: list):
        self.domains = domains
        self.mails = mails
        self.min_length = min_length

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        # regex = r'(?P<name>\w+@)(?P<mail>[a-z]+\.)(?P<domain>[a-z]+)'
        # data = match(regex, email).groupdict()
        # data['name'] = data['name'][:-1]
        # data['mail'] = data['mail'][:-1]
        tokens = email.split('@')
        name = tokens[0]
        tokens2 = tokens[1].split('.')
        mail = tokens2[0]
        domain = tokens2[1]
        return True if self.__is_name_valid(name) and self.__is_mail_valid(mail) and \
                       self.__is_domain_valid(domain) else False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
