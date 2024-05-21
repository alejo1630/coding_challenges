# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    
    return sum(list(map(sentence.count, "aeiou")))



example = "hello world my name is alejandro"

print(get_count(example))