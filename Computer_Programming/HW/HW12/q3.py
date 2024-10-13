import itertools

def product_sets(*sets):
    result = itertools.product(*sets)
    set_result = set(result)
    return set_result

s1 = {1,2,3}
s2 = {'p','q'}
s3 = {'a','b','c'}
print(product_sets(s1,s2,s3))