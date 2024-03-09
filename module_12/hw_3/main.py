# importing py files
from classes.address_book import AddressBook
from functions.command_func import add_contact
from functions.command_func import change_contact
from functions.command_func import add_birthday
from functions.command_func import show_phone
from functions.command_func import show_birthday
from functions.command_func import show_all
from functions.command_func import birthdays
from functions.load_contacts import load_contacts



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    loaded_contacts = load_contacts()
    if loaded_contacts:
        contacts = loaded_contacts
    else:
        contacts = AddressBook()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye:)Have a nice day!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "change":
            print(change_contact(args,contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()