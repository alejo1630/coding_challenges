# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python


def digital_root(n):

    dig_sum = sum([int(i) for i in str(n)])
    while dig_sum > 9:
        dig_sum = sum([int(i) for i in str(dig_sum)])
    
    return dig_sum




print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
print(digital_root(2493667))
