def nyah (x):
    total = 0
    for i in x:
        if i.isdigit():
            i = int(i)
            total += i
    print(total)
1
nyah("23meownyah4")