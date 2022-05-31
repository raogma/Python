class DVD:
    def __init__(self, name, id, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) \
has age restriction {self.age_restriction}. Status: {status}"

    @classmethod
    def from_date(cls, id, name, date: str, age_restriction):
        day, month, year = date.split('.')
        return cls(name, id, int(year), cls.convert_month(int(month)), age_restriction)

    @staticmethod
    def convert_month(num):
        info = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                'October', 'November', 'December'
                )
        return info[num - 1]
