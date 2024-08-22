import random
def print_score(a):
    grade = ""
    if 80 <= a <= 100:
        grade = "A"
    elif 70<= a < 80:
        grade = "B"
    elif 60<= a < 70:
        grade = "C"
    elif 50<= a < 60:
        grade = "D"
    elif 0<= a < 50:
        grade = "F"
    else:
        grade = "Invalid nyan"
    print(grade)

for i in range(10):
    print_score(random.randint(50,100))