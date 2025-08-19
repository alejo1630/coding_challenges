
# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python


# def diamond(n):
#     # Make some diamonds!
#     return "*"

n = 5
center = "*" * n
list_d = [center]
conteo = center.count("*")

while conteo > 1:
    center = " " + center[:-1]
    list_d.insert(0, center)
    list_d.append(center)
    conteo = center.count("*")


print(list_d)

