#coding challenge

def greet (name):
    print(f"Hello {name}")

greet("Emil")


def calculate_total(price, quantity):
    cost = price * quantity
    return cost

calculate_total(15, 4)

def calculate_grade(mark, total):
    percentage = (mark/total) * 100

    if percentage >= 70:
        return "A" 
    elif percentage >= 60:
        return "B"
    elif percentage >=50:
        return "C"
    else:
        return "U"

print(calculate_grade(54,100))