searched_book = input()
book = input()
book_counter = 0

while book != "No More Books":
    if book == searched_book:
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1
    book = input()

else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
