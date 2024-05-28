# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    
    mod = [i%2 for i in integers]

    if sum(mod) == 1:
        return integers[mod.index(1)]

    else:
        return integers[mod.index(0)]


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))