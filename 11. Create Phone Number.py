# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python


def create_phone_number(n):
    
    return f"({''.join(list(map(str, n[0:3])))}) {''.join(list(map(str, n[3:6])))}-{''.join(list(map(str, n[6:])))}"



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

