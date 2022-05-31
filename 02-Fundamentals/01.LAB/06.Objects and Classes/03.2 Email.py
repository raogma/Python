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


emails = []

while True:
    command = input()
    if command == 'Stop':
        break
    tokens = command.split()
    sender = tokens[0]
    receiver = tokens[1]
    msg = tokens[2]
    email = Email(sender, receiver, msg)
    emails.append(email)

indices = input().split(', ')
indices_int = list(map(lambda x: int(x), indices))

for element in indices_int:
    emails[element].send()

for piece in emails:
    print(piece.get_info())