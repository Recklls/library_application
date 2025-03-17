book_list = list()
menu = """
1) Add Book:
2) Remove Book:
3) View Books:
4) Press Q to Exit
"""

def add_book(booklist, book):
    booklist += [book]
    print(input("Enter the name of the book to add"))
    print("Book added successfully")

def remove_book():
    pass

def display_list(booklist):
    for book in booklist:
        print("Added Books ->", book)

def exit_program():
    print("Thank you for choosing us. :)")
    quit()

while True:
    print(menu)
    choice = input("Your Choice:")
    if choice == "1":
        book_name = input("Book name:")
    elif choice == "2":
        print(remove_book())
        input("Enter the book to remove:")
    elif choice == "3":
        print(book_list)
    elif input("Q" or "q"):
        exit_program()
    else:
        print("Invalid entry")
        input("Press Enter to return to the main menu!")
