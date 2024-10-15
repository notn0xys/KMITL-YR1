def get_sum(l:list,current_sub= [],index = 0,return_list = []):
    if index == len(l):
        if sum(current_sub) == 0 and len(current_sub) != 0:
            return_list.append(current_sub.copy())
        return 
    current_sub.append(l[index])
    get_sum(l,current_sub,index + 1,return_list)
    current_sub.pop()
    get_sum(l,current_sub,index + 1,return_list)
    if index == 0 and len(return_list) != 0:
        print("Yes", end="")
        print(return_list)
    elif index == 0:
        print("No")
get_sum([7,-3,-2,5,-7])
