def nyah (x):
    x = str(x)
    total = 0
    for i in x:
        if i.isdigit():
            i = int(i)
            total += i
    print(total)

nyah("")