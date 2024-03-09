# book = AddressBook()
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday("12.02.1989")


#  print(john_record.name)
#  print(john_record.phones)

# book.add_record(john_record)


# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_birthday("18.02.1991")
# book.add_record(jane_record)

# print(jane_record.name)
# print(jane_record.phones)

# for name, record in book.data.items():
#         print(record)

# john = book.find_record("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)

# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")

# result = book.delete_record("Jane")
# print(result)


# Test the function with sample data
# data = AddressBook()
# data.add_record('Alice', datetime(2023, 8, 1))  
# data.add_record('Bob', datetime(2023, 8, 3))    

# data.get_birthdays_per_week()

# #test bot
# "add": add Bob 1868920007
#        add Bob 1233444
#        add Bob 1233h66677
#        add 1234567890
# "add-birthday":
#        add Bob 20.01.91
#        add 20.01.1991
#        add Bob 20.01.1991
# "change":
#        change Viki 1234567890
#        change Bob
#        change Bob 13456765678
# "phone":
#        phone
#        phone Viki
#        phone Bob
# "show-birthday":
#        show-birthday Viki
#        show-birthday Bob

