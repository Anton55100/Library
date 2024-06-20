import sys
from book import Book
from library import Library
from user import User


def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    return User(username, password)


def main():
    library_instance = Library()
    user_instance = None

    while True:
        print("1. Create account")
        print("2. Login")
        print("3. Exit")

        option = input("Enter option: ")

        if option == "1":
            user_instance = create_account()
            print("Account created!")
        elif option == "2":
            if not user_instance:
                print("Please create an account first!")
                continue
            username = input("Enter username: ")
            password = input("Enter password: ")
            if (
                username == user_instance.username
                and password == user_instance.password
            ):
                print("Authenticated!")
                while True:
                    print("1. Add book")
                    print("2. Remove book")
                    print("3. Display books")
                    print("4. Search book")
                    print("5. Logout")
                    print("6. Exit")

                    option = input("Enter option: ")

                    if option == "1":
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        year = input("Enter book year: ")
                        book = Book(title, author, year)
                        library_instance.add_book(book)
                    elif option == "2":
                        if not library_instance.books:
                            library_instance.display_books()
                        else:
                            title = input("Enter book title: ")
                            library_instance.remove_book(title)
                    elif option == "3":
                        library_instance.display_books()
                    elif option == "4":
                        if not library_instance.books:
                            library_instance.display_books()
                        else:
                            title = input("Enter book title: ")
                            library_instance.search_book(title)
                    elif option == "5":
                        print("Logged out!")
                        break
                    elif option == "6":
                        sys.exit(0)
                    else:
                        print("Invalid option!")
            else:
                print("Invalid username or password. Please try again.")
        elif option == "3":
            sys.exit(0)
        else:
            print("Invalid option!")


main()
