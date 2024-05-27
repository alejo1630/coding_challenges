# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python


def likes(names):
    if len(names) == 0:
        return "no one likes this"

    elif len(names) == 1:
        return f"{names[0]} likes this"

    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"






print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))