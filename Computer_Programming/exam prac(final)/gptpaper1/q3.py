def fibonachi(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonachi(x - 1) + fibonachi(x - 2)
for i in range(10):
    print(f"Fibinaci {i} , {fibonachi(i)}")