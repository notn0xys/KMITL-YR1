

while True:
    x = input("Type in a single character: ")
    if len(x) == 1:
        break
    print("Not a single character   ")
y = ord(x)


print("u"+'%04x' % y)