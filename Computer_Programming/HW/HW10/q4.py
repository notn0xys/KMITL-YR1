def print_table(x:list):
    ajust = []
    for i in range(len(x[0])):
        max = 0
        for j in range(len(x)):
            if len(str(x[j][i])) > max:
                max = len(str(x[j][i])) 
        ajust.append(max)
    for i in range(len(ajust)):
        ajust[i] += 1
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(str(x[i][j]).ljust(ajust[j]),end = "")
        print()
print_table([["X","Y"],[0,0],[10,10],[100,100]])
print()
print_table([["ID","Name","Surname"],["001","NyanNyan :3","JJomez"],["002","Meow","Mahahahaha"],["003","XD","Test"]])