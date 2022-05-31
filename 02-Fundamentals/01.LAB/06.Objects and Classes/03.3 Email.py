class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.isSent = False

    def send(self):
        self.isSent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.isSent}"


class Mailbox:
    def __init__(self):
        self.email_list = []

    def append_email(self, email):
        self.email_list.append(email)

    def send_emails(self, indices):
        for i in indices:
            self.email_list[i].send()

    def get_all_info(self):
        all_info = ''
        for email in self.email_list:
            all_info += f'{email.get_info()}\n'
        return all_info


mailbox = Mailbox()

while True:
    command = input()
    if command == 'Stop':
        break
    sender, receiver, msg = command.split(' ', maxsplit=2)  ############
    email = Email(sender, receiver, msg)
    mailbox.append_email(email)

indices = [int(j) for j in input().split(', ')]
mailbox.send_emails(indices)
print(mailbox.get_all_info())
