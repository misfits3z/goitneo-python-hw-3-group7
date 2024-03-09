
from collections import UserDict
from datetime import datetime, timedelta
from collections import defaultdict
from functions.save_contacts import save_contacts




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
        
class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday



class Record:
    def __init__(self, name, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print("Phone number already exists for this contact")

    def get_birthday(self):
        if self.birthday:
            return self.birthday
        else:
            return "Birthday not set for this contact"
    

    def add_birthday(self, birthday):
        try:
            parsed_birthday = datetime.strptime(birthday, '%d.%m.%Y')
            self.birthday = parsed_birthday
        except ValueError:
            raise ValueError("Data must have format DD.MM.YY")


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
        return f"Contact name: {self.name},  Phones: {phone_str}"

   
class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name not in self.data:
            self.data[record.name] = record
            print(f'Contact {record.name} added to contacts')
            save_contacts(self.data)
        else:
            print(f'Contact with name {record.name} already exist ')

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
        
      
    def get_birthdays_per_week(self):
        weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        birthdays = defaultdict(list)
        today = datetime.now()

        for name, record in self.data.items():
            if record.birthday:
                birthday_this_year = record.birthday.strftime('%d.%m.%Y')  # Convert datetime object to string
                birthday_this_year = datetime.strptime(birthday_this_year, '%d.%m.%Y')
                birthday_this_year = birthday_this_year.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if birthday_this_year.weekday() >= 5:
                    delta_days = 7 - birthday_this_year.weekday()
                    birthday_this_year += timedelta(days=delta_days)
        
                weekday = weekdays[birthday_this_year.weekday()]
                birthdays[weekday].append(name)
                
        if not birthdays:
            print("No birthdays next week")
        else:
            for day, names in birthdays.items():
                print(f'{day}: {','.join(names)}')


    

# book = AddressBook()
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday("12.02.1989")


# # print(john_record.name)
# # print(john_record.phones)

# book.add_record(john_record)


# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_birthday("18.02.1991")
# book.add_record(jane_record)

# # print(jane_record.name)
# # print(jane_record.phones)

# for name, record in book.data.items():
#         print(record)

# john = book.find_record("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)

# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")

# result = book.delete_record("Jane")
# print(result)

