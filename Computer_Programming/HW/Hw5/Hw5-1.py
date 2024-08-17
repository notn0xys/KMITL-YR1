while True:
    n = input("Enter a positive number: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Not 0")
    else:
        print("Try agian")
guess = n / 2
time5 = 0
time6 = 0
time7 = 0
for i in range(7):
    temp = n / guess
    guess = (guess + temp) / 2
    if i == 4:
        time5 = guess
    if i == 5:
        time6 = guess
    if i == 6:
        time7 = guess
print(f"When done 5 times you get {time5:.3f} ")
print(f"When done 6 times you get {time6:.3f} ")
print(f"When done 7 times you get {time7:.3f} ")
print("The result is that when done 5,6,7 times and round up the decimal points the values are the same")