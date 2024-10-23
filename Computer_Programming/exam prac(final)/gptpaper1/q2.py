def rank_employees(employee_salaries:dict):
    sorted_dict = dict(sorted(employee_salaries.items(), key = lambda item: item[1], reverse= True))
    return list(sorted_dict.keys())
print(rank_employees({'Alice': 50000, 'Bob': 45000, 'Eve': 50000}))