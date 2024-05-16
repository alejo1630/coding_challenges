
#https://www.codewars.com/kata/5264d2b162488dc400000001


def spin_words(sentence):

    final_words = []

    for word in sentence.split():
        if len(word) >= 5:
            final_words.append(word[-1::-1])
        else:
            final_words.append(word)
    
    return (" ".join(final_words))


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))

