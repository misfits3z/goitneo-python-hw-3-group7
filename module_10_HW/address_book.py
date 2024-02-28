
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, phone_number):
        super().__init__(phone_number)

    def format_number(self):
        if len(self.value) == 10 and self.value.isdigit():
            return True
        else:
            return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print("Phone number already exists for this contact")

    def delete_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print("Phone number not found for this contact")

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones[index] = new_phone
        else:
            print("Phone number not found for this contact")

    def find_phone(self, phone):
        if phone in self.phones:
            print(f"{phone} found in the list of phone numbers for {self.name}")
        else:
            print(f"{phone} not found in the list of phone numbers for {self.name}")

    def __str__(self):
        phone_str = ', '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, Phones: {phone_str}"
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, name):
       if name in self.data:
            return self.data[name]
       else:
            return print(f"Record with name {name} not found")

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record with name '{name}' deleted"
        else:
            return f"Record with name '{name}' not found"

    

book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# print(john_record.name)
# print(john_record.phones)

book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# print(jane_record.name)
# print(jane_record.phones)

for name, record in book.data.items():
        print(record)

john = book.find_record("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

result = book.delete_record("Jane")
print(result)