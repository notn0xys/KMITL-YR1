def remove_third(l: list):
    n = 0
    for i in range(len(l)):
        if (i + 1 ) % 3 == 0:
            l.pop(i - n)
            n += 1
list_on = [3,6,6,3,7,2,0,1,5,4]
remove_third(list_on)
print(list_on)