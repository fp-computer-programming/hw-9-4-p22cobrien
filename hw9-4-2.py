# Author: CMOB 1/14/2022

def products(lst, value_1):
    up_lst = []
    for index, value in enumerate(lst):
        up_lst.append(value * value_1)
    return up_lst



print(products([1,2,3,4,5,6,7,8,9], 2))
            
