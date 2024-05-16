

#https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):

    multiples = []

    if number < 0:

        return 0

    else:

        for i in range(number):
            if i%5 == 0:
                multiples.append(i)
            
            if i%3 == 0:
                multiples.append(i)

        return sum(set(multiples))


print(solution(1))
print(solution(2))
print(solution(4))
print(solution(10))
print(solution(20))

  