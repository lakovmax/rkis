list1 = [6,3,4]
def change(lst):
    lst = lst[:]
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change(list1))