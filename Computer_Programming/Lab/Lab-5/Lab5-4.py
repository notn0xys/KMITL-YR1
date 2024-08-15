# num = 1
# i = 0
# while num <= 49:
#     print(num)
#     if i % 2 == 0:
#         num += 1
#     else:
#         num += 2
#     i += 1

for i in range(50):
    if i % 3 == 0:
        continue
    print(i, end="")
    if i != 49:
        print(", ",end="")
    else:
        print(".")
    