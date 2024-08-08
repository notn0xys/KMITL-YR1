Old = True
store = 0
for i in range(5):
    meow = 0
    if i > 0:
        meow = int(input("Enter an integer: "))
        isNegative = meow < 0 
        if Old != isNegative:
            store = meow
        else:
            store += meow
        print(store)
        Old = isNegative
        
    else:
        meow = int(input("Enter an integer: "))
        isNegative = meow < 0 
        Old = isNegative
        store += meow
        print(store)
