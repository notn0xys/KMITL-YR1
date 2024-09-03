bills1k = 0
bills500 = 0
bills100 = 0
bills50 = 0
bills20 = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0
amount = int(input("enter the amount of money you wish to withdraw: "))
list_of_bills = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
coin = False
list_of_var = [bills1k,bills500, bills100, bills50, bills20, coin10, coin5, coin2, coin1]
for i in range(len(list_of_bills)):
    list_of_var[i] = amount // list_of_bills[i]
    amount -= list_of_var[i] * list_of_bills[i]
for i in range(len(list_of_bills)):
    if i > 3:
        coin = True
    if coin:
        print(f"{list_of_bills[i]} Coin : {list_of_var[i]}")
    else:
        print(f"{list_of_bills[i]} Bills : {list_of_var[i]}")