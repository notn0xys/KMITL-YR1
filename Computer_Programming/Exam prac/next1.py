amount = int(input("enter the amount of money you wish to withdraw: "))
bills1k = amount // 1000
amount -= 1000*bills1k
bills500 = amount//500
amount -= 500*bills500
bills100 = amount//100
amount -= bills100*100
print("You get: ",end="")
if bills1k > 0:
    print(f"{bills1k} Notes of 1000 Baths")
if bills500 > 0:
    if bills1k != 0:
        print(f"         ",end="")
    print(f"{bills500} Notes of 500 Baths")
if bills100 > 0:
    if bills1k != 0 or bills500 != 0:
        print(f"         ",end="")
    print(f"{bills100} Notes of 100 Baths")

