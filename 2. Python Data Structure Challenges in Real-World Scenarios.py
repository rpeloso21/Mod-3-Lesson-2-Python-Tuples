# Task 1



def add_book(library, book):
    for item in library:
        if item[0] == book[0]:
            return print('That item is already in library.')

    library.append(book)


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_book = ("The Name of the Wind", "Pat Rothfus")
new_book2 = ("The Name of the Wind", "Pat Rothfus")


add_book(library, new_book)
add_book(library, new_book2)


print(library)