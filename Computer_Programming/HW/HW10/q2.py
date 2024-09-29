def bubble(x:list):
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                x[j] , x[j + 1] = x[j + 1] , x[j]
x = [3,2,9,7,8]
bubble(x)
print(x)