# Bài 4
s = input()
upper = lower = digit = special = space = vowel = consonant = 0
for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
    if c.isdigit():
        digit += 1
    elif not c.isalnum() and not c.isspace():
        special += 1
    if c.isspace():
        space += 1
    if c.lower() in "aeiou":
        vowel += 1
    elif c.isalpha():
        consonant += 1

print(upper)
print(lower)
print(digit)
print(special)
print(space)
print(vowel)
print(consonant)