# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c



def duplicate_encode(word):
    return "".join(["(" if x == 1 else ")" for x in [word.lower().count(i) for i in word.lower()]])


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))