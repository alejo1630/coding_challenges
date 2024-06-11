
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):

    lst_2 = [i for i in lst if i  !=0]
    lst_2.extend([0] * lst.count(0))

    return lst_2


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

