class FormatterMixin:
    @staticmethod
    def edit(new_content, book: object) -> str:
        return book.content + new_content


class PrinterMixin:
    @staticmethod
    def get_book_content(book: object) -> str:
        return book.content


class Book:
    def __init__(self, content: str):
        self.content = content
        self.formatter = FormatterMixin()
        self.printer = PrinterMixin()

    def publish(self):
        return self.printer.get_book_content(self)

    def format(self, new_content):
        self.content = self.formatter.edit(new_content, self)


# no format
b = Book('gosho')
print(b.publish())

# format
b.format('pesho')
print(b.publish())