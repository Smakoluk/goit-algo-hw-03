import random

v_min = int(input(""))
v_max = int(input(""))
quantity = int(input(""))

def get_numbers_ticket(v_min, v_max, quantity):
    
        if v_min <= 1 and v_max >= 1000 and quantity <= 0:
            return []
        else: 
            return sorted(random.sample(range(v_min, v_max + 1), quantity))
    
 
lottery_numbers = get_numbers_ticket(v_min, v_max, quantity)
print(f"Ось список білетів :", lottery_numbers)

    

    

