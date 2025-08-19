'''
https://leetcode.com/problems/palindrome-number/description/

Given an integer x, return true if x is a palindrome, and false otherwise.

'''


def isPalindome(x: int):
    x_str = str(x)
    x_inv = x_str[::-1]

    if x_str == x_inv:
        return True

    else:
        return False


print(isPalindome(121))
print(isPalindome(10))
print(isPalindome(-121))
