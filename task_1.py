from datetime import datetime

date = str(input("Вкажіть дату у форматі: РРРР-ММ-ДД " ))

def get_days_from_today(date):
        

    
    try:

        date_then = datetime.strptime(date, "%Y-%m-%d").date()

        today = datetime.now().date()

        difference = today - date_then


        return difference.days
    
    except ValueError:
         print("Неправильний формат дати,будь ласка,дотримуйтесь інструкції")
    return None

    

days_difference = get_days_from_today(date)
if days_difference is not None:
    print(f"Кількість днів між {date} та сьогодні: {days_difference}")




   

        
    
    

        
        
         

        
