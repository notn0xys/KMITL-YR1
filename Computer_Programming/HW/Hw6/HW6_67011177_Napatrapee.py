#q1
def time(x):
    new = x.split(":")
    hr = int(new[0])
    minutes = int(new[1])
    if hr > 23 or minutes > 59:
        return "Invalid hour"
    after = ""
    if hr >= 12 and hr != 24:
        after = "PM"
        if hr == 12:
            hr = 12
        else:
            hr -= 12
    elif hr == 24:
        after = "AM"
        hr = 0
    else:
        after = "AM"
    if hr < 10:
        newhr = "0" + str(hr)
    else:
        newhr = str(hr)
    if minutes < 10:
        newminutes = "0" + str(minutes)
    else:
        newminutes = str(minutes)
    total = newhr + ":" + newminutes + " " + after
    return total
print(time("23:24"))
#q2
from turtle import *
def go_back(l,h):
    backward(l * 7)
    right(90)
    forward(h)
    left(90)
def draw_box(l,h):
    for j in range(2):
        forward(l)
        left(90)
        forward(h)
        left(90)

def calendar_of_2024(n):
    if n > 12:
        print("Invalid Month")
        return "invalid Month"
    mo_dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    tracker = 1
    start_date = [0,3,4,0,2,5,0,3,6,1,4,6]
    dates = ["Mo", "Tu", "W", "Th", "Fr", "Sa","Su"]
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", " December"]
    display_month = months[n-1] + " 2024"
    l = 30
    h = 20
    if n == 9 or n == 12:
        row = 8
    else:
        row = 7
    for i in range(row):
        if i == 0:
            for k in range(2):
                forward(l * 7)
                left(90)
                forward(h)
                left(90)
            print(len(display_month))
            forward((l * 7/2) - (len(display_month)* 2) -5 )
            write(display_month)
            backward((l * 7/2) - (len(display_month) * 2) -5)
            right(90)
            forward(h)
            left(90)
        elif i == 1:
            for k in range(7):
                draw_box(l,h)
                forward(l/4)
                write(dates[k])
                forward(3*l / 4)
            go_back(l,h)
        elif i == 2:
            for k in range(7):
                draw_box(l,h)
                forward(l/4)
                if k >= start_date[n-1]:
                    write(tracker)
                    tracker += 1
                forward(3*l / 4)
            go_back(l,h)
        else:
            for k in range(7):
                draw_box(l,h)
                forward(l/4)
                if tracker <= mo_dates[n-1]:
                    write(tracker)
                    tracker += 1
                forward(3*l / 4)
            if i != row - 1:
                go_back(l,h)
            else:
                backward(l*7)
    return None
speed("fastest")
calendar_of_2024(8)
done()
#q3
while True:
    n = input("Enter a number: ")
    if n.isdigit():
        n = int(n)
        break
if n >= 0 and n <= 999:
    list_of_digits = ["one","two","three","four","five","six","seven","eight","nine"]
    list_of_tens = ["eleven","twelve","thriteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    list_of_tys = ["ten","twenty","thrity","forty","fifty","sixty","seventy","eighty","ninety"]
    hundread = n//100
    n = n - (hundread * 100)
    tens = n//10
    n = n - (tens * 10)

    if hundread > 0:
        print(f"{list_of_digits[hundread-1]} hundred ",end="")
        if tens > 0 or n > 0:
            print("and " , end="")
    if tens == 1:
        if n > 0:
            print(f"{list_of_tens[n-1]} ")
        else:
            print(f"{list_of_tys[0]} ")
    else: 
        if tens > 1:
            print(f"{list_of_tys[tens-1]}" , end="")
            if n > 0:
                print("-",end="")
        if n > 0:
            print(f"{list_of_digits[n-1]} ")
    if hundread == 0 and tens == 0 and n == 0:
        print("zero")           
else:
    print("I dont know")
#q4
bills1k = 0
bills500 = 0
bills100 = 0
bills50 = 0
bills20 = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0
while True:
    amount = input("enter the amount of money you wish to withdraw: ")
    if amount.isdigit():
        amount = int(amount)
        break
    print("try agian")

list_of_bills = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
coin = False
list_of_var = [bills1k,bills500, bills100, bills50, bills20, coin10, coin5, coin2, coin1]
for i in range(len(list_of_bills)):
    list_of_var[i] = amount // list_of_bills[i]
    amount -= list_of_var[i] * list_of_bills[i]
for i in range(len(list_of_bills)):
    if i > 4:
        coin = True
    if coin and list_of_var[i] > 0:
        print(f"{list_of_bills[i]} Coin : {list_of_var[i]}")
    elif coin == False and list_of_var[i] > 0:
        print(f"{list_of_bills[i]} Bills : {list_of_var[i]}")
#q5
def reverse(x):
    x = str(x)
    x = x[::-1]
    return int(x)

print(reverse(1233))