def find_num(num,list_of_nums):
    return_list = []
    for i in range(len(list_of_nums)):
        if num == list_of_nums[i]:
            return_list.append(i)
    return return_list if len(return_list) != 0 else 0
print(find_num(2 ,[1,2,3,4,5,6,2]))