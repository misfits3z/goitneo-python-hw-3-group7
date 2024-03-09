from classes.address_book import AddressBook, Record
from datetime import datetime

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
    elif len(phone) != 10:
        raise ValueError("Phone number should have exactly 10 digits.")
    elif not name.isalpha():
        raise ValueError("Name must be a text, not number")
    elif name in contacts:
        raise ValueError(f'This name already in contacts.\nType "phone {name}" to check.')  
    else:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
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

    for i, (name, record) in enumerate(contacts.items(), start=1):
        phones = record.phones
        birthday = record.birthday
        formatted_str = f'{i:>5}.{name:<5} Phone: {str(phones):>5}'

        if birthday:
            formatted_str += f' Birthday: {birthday.strftime('%d.%m.%Y'):>5}'

        all_contacts.append(formatted_str)
    return all_contacts


@input_error
def add_birthday(args, contacts):
    if len(args) < 2:
        raise ValueError("Give me name and date please")
    name, birthday = args

    if name not in contacts:
        raise KeyError("Contact not found")
    
    try:
        datetime.strptime(birthday, '%d.%m.%Y')
    except ValueError:
        raise ValueError("Date must have format DD.MM.YYYY")
    else:
        contact = contacts.get(name)
        contact.add_birthday(birthday)
        print(f"Birthday added for {name}.")
    

@input_error
def show_birthday(args, contacts):
    name, = args
    if name in contacts:
        contact = contacts.get(name)
        birthday = contact.get_birthday()
        return f"{name}'s birthday on {birthday.strftime('%d.%m.%Y')}."  #birthday.strftime('%d.%m.%Y')
    else:
       raise KeyError('Birthday not found') 
    
@input_error 
def birthdays(contacts):
    if not contacts:
        raise IndexError
    else:
        address_book = AddressBook(contacts)
    
    birthdays_per_week = address_book.get_birthdays_per_week()
    
    if birthdays_per_week is not None:
        birthdays_dict = {key: value for key, value in birthdays_per_week.items()}
        return birthdays_dict
    




