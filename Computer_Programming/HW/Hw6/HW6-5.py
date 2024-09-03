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