
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e
        except KeyError: 
            return "No contacts with such name found!"
        except IndexError:
            return "Contacts not found!"
    return inner

    

  

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Give me name and phone number please")
    name, phone = args
    if not phone.isdigit():
        raise ValueError("Phone number should contain only digits.")
    elif not name.isalpha():
        raise ValueError("Name must be a text, not number")
    elif name in contacts:
        raise ValueError(f'This name already in contacts.\nType "phone {name}" to check.')
    else:
         contacts[name] = phone
    return f"Contact added. Name - {name}, phone - {phone}"

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Give me name and phone number please")
    name, new_phone = args
    if name not in contacts:
       raise KeyError
    if not new_phone.isdigit():
        raise ValueError("Phone number should contain only digits.")
    else:
       contacts[name] = new_phone
       return f"Contact updated.Name - {name}, phone - {new_phone}"
  

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError
    else:
       return contacts.get(name)
   
   
@input_error
def show_all(contacts):
    if not contacts:
        raise IndexError
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