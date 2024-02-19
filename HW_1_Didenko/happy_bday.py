
from collections import defaultdict
from datetime import datetime

def get_birthdays_per_week(users):
    weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    birthdays = defaultdict(list)
    
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        
        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()
            if day_of_week > 4:
                day_of_week = 0
            
            birthdays[weekdays[day_of_week]].append(name)
    
    return birthdays

users = [{'name': 'Bill Gates', 'birthday': datetime(1955, 10, 28)},
          {'name': 'Steve Jobs', 'birthday': datetime(1955, 2, 24)},
          {'name': 'Dog Pug', 'birthday': datetime(2022, 2, 19)},
          {'name': 'Mark Zuckerberg', 'birthday': datetime(1984, 5, 14)}]

birthdays_per_week = get_birthdays_per_week(users)

for day, names in birthdays_per_week.items():
    if names:
        print(f"{day}: {', '.join(names)}")
    else:
        print(f"No birthdays on {day}")





        