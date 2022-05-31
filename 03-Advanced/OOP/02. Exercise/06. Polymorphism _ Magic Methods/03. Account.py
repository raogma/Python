from typing import Optional


class Account:
    def __init__(self, owner, amount: Optional[int] = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: object, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.amount += amount_to_add
        return f"New balance: {account.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    def __str__(self):
        class_name = self.__class__.__name__
        owner = self.owner
        balance = self.amount
        return f'{class_name} of {owner} with starting amount: {balance}'

    def __repr__(self):
        class_name = self.__class__.__name__
        owner = self.owner
        balance = self.amount
        return f'{class_name}({owner}, {balance})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, key):
        return self._transactions[key]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __neg__(self):
        return self.amount != other.amount

    def __add__(self, other):
        total_owners = f'{self.owner}&{other.owner}'
        total_amount = self.amount + other.amount
        total_transactions = self._transactions + other._transactions
        new_account = Account(total_owners, total_amount)
        new_account._transactions.extend(total_transactions)
        return new_account