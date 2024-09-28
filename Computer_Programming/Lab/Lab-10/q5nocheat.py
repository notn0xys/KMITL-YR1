def merge(l1:list,l2:list):
    l1_longer = None
    l3 = []
    i = 0
    j = 0
    if len(l1) > len(l2):
        l1_longer = True
    else:
        l1_longer = False