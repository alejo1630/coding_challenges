# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python


def mul_list(digits):
    product = 1

    for i in digits:
        product = product * i

    return product

def persistence(n):
    if n < 10:
        return 0
    else:
        cont = 1
        while mul_list([int(i) for i in str(n)]) > 9:
            n = mul_list([int(i) for i in str(n)])
            cont += 1

        return cont






print(persistence(39))
print(persistence(999))
print(persistence(4))
print(persistence(25))