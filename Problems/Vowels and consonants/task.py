entry = input()
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

for character in entry:
    if character in vowels:
        print("vowel")
        continue
    if character in consonants:
        print("consonant")
    else:
        break
