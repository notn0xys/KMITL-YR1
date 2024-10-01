#Q1
import matplotlib.pyplot as plt 
def pie_chart(x:list):
    nyan1 = dict()
    for i in x:
        if i not in nyan1:
            nyan1[i] = 1
        else:
            nyan1[i] += 1
    plt.pie(nyan1.values())
    plt.show() 
pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])
#Q2
def bubble(x:list):
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                x[j] , x[j + 1] = x[j + 1] , x[j]
x = [3,2,9,7,8]
bubble(x)
print(x)
#Q3
def my_union(l1:list,l2:list) -> list:
    l3 = l1 + l2
    l4 = []
    for i in l3:
        if i not in l4:
            l4.append(i)
        else:
            continue
    return l4
def my_intersec(l1:list,l2:list) -> list:
    l3 = [i for i in l1 if i in l2]
    return l3
def my_diff(l1:list,l2:list) -> list:
    l3 = [i for i in l1 if i not in l2]
    return l3
list1 = [3,1,2,4,7]
list2 = [4,1,2,5,7]
print(my_union(list1,list2))
print(my_intersec(list1,list2))
print(my_diff(list1,list2))
#Q4
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
#Q5
def isAnagram(s1:str,s2:str):
    nyan1 = dict()
    nyan2 = dict()
    for i in s1:
        if i not in nyan1:
            nyan1[i] = 1
        else:
            nyan1[i] += 1
    for i in s2:
        if i not in nyan2:
         nyan2[i] = 1
        else:
         nyan2[i] += 1
    if nyan1 != nyan2:
       return False
    else:
       return True
print(isAnagram("silent","listen"))