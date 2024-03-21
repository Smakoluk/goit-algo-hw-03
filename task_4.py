from datetime import datetime, timedelta


users = [
    {"name": "Tony Stark", "birthday": "1984.05.23"},
    {"name": "Will Smith", "birthday": "1990.09.27"},
    {"name": "Tina Karol", "birthday": "1974.03.25"}

]



def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

    birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

    if birthday_this_year < today:
        birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()

        
        
    days_till_birthday = (birthday_this_year - today).days


    if 0 <= days_till_birthday <= 7:
            
            if birthday_this_year.weekday() in [5, 6]:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
                                    
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})
            
            
            return upcoming_birthdays
 

upcoming_birthdays = get_upcoming_birthdays(users)
for user in upcoming_birthdays:
     print(f"У {user['name']} день народження: {user['congratulation_date']}")






