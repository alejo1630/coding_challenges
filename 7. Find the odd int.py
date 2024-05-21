# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python


def find_it(seq):

    return [i[0] for i in set(zip(seq,map(seq.count, seq))) if i[1]%2 != 0][0]





print(find_it([7]))
print(find_it([0]))
print(find_it([1,1,2]))
print(find_it([0,1,0,1,0]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))