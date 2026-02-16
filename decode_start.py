alphabet = " abcdefghijklmnopqrstuvwxyz"   # index: 0=' ', 1='a', ... 26='z'
vowel = "aeiou"
message = ""

with open("secret.txt") as f:
    for line in f:
        nr_vowels = 0
        for v in vowel:
            nr_vowels += line.count(v) # count the num. of times that a particular vowel shows up
        letter = alphabet[nr_vowels]
        message += alphabet[nr_vowels]

    print(message)

