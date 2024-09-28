def name_list():
    i = 1
    lon = []
    while True:
        x = input(f"Enter Name {i}: ")
        if x == "":
            break
        lon.append(x)
        i += 1
    print(lon)
name_list()
