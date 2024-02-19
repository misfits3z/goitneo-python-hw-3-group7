def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
       contacts[name] = new_phone
       return "Contact updated."
    else:
        return f"{name} not found!"

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts.get(name)  
    else:
        return f"Phone number not found for {name}"

def show_all(contacts):
    all_contacts = []
    for i, (name, phone) in enumerate(contacts.items(), start=1):
        formatted_str = f'{i:>5}.{name:<5}:{phone:>5}'
        all_contacts.append(formatted_str)
    return all_contacts
    
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
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
        elif command == "change":
            print(change_contact(args,contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    