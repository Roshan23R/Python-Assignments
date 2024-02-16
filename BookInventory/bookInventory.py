def add_book():
    '''Process of adding the book to inventory'''

    print(add_book.__doc__)
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    copies = input("Enter the number of copies available: ")

    with open("library_inventory.txt", "a",encoding="utf8") as file:
        file.write(f"{title},{author},{genre},{copies}\n")
    print("Book added successfully!")

def view_inventory():
    '''View the books in Inventory'''

    print(view_inventory.__doc__)
    try:
        with open("library_inventory.txt", "r",encoding="utf8") as file:
            print("{:<25} {:<25} {:<20} {:<7}".format("Title", "Author", "Genre", "Copies"))
            print("-" * 82)  # Line separator
            for line in file:
                title, author, genre, copies = line.strip().split(',')
                print("{:<25} {:<25} {:<20} {:<7}".format(title, author, genre, copies))
    except:
        print("No Book Found")  

def search_book():
    '''Search book and get the details'''

    title_to_search = input("Enter the title of the book to search: ")
    found = False

    try:
        with open("library_inventory.txt", "r",encoding="utf8") as file:
            for line in file:
                if title_to_search in line:
                    title, author, genre, copies = line.strip().split(',')
                    print("Book found:")
                    print("{:<25} {:<25} {:<20} {:<7}".format(title, author, genre, copies))
                    found = True
                    break
            if not found:
                print("Book not found!")
    except FileNotFoundError:
        print("Inventory file not found!")
def update_inventory():
    '''Update the copies of a book'''
    book_title = input("Enter the title of the book to update: ")
    new_copies = input("Enter the new number of copies available: ")
    updated = False

    try:
        with open("library_inventory.txt", "r",encoding="utf8") as file:
            lines = file.readlines()
        with open("library_inventory.txt", "w", encoding="utf8") as file:
            for line in lines:
                if book_title in line:
                    updated_line = line.strip().split(',')
                    updated_line[-1] = f"{new_copies}\n"
                    file.write(','.join(updated_line))
                    updated = True
                else:
                    file.write(line)
        if updated:
            print("Inventory updated successfully!")
        else:
            print("Book not found!")
    except FileNotFoundError:
        print("Inventory file not found!")


# Main function to provide menu-driven interface
def main():
    print("Welcome to the Library Management System")
    print("1. Add Book")
    print("2. View Inventory")
    print("3. Search Book")
    print("4. Update Inventory")
    print("5. Exit")
    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_inventory()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()