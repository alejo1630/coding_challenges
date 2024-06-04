# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python


def count_bits(n):
    return sum(map(int, list(map(str, bin(n)))[2:]))


print(count_bits(1234))
print(count_bits(783))
print(count_bits(2053594))
