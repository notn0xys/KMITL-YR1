long_str = input("Enter long string: ").strip()
short_str = input("Enter short String: ").strip()
points = []
total_check = 1
side = False
for i in range(len(long_str)):
    if short_str[0] == long_str[i]:
        points.append(i)
print(points)
for i in points:
    for j in range(1,len(short_str)):
        if i + j > len(long_str) - 1:
            break
        if long_str[i + j] != short_str[j]:
            print("Not same")
        else:
            print("same")
            total_check += 1
        if total_check == len(short_str):
            side = True
        if side:
            break
    total_check = 1
if side:
    print("It is inside")
else:
    print("Not inside")


            


