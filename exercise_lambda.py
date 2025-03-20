# Una función que cuente la ocurrencia de un caracter en una frase

phrase = 'aprendiendo python'
char_to_count = 'y'

def count_char(phrase, char_to_count):
    count = 0
    for char in phrase:
        if char == char_to_count:
            count += 1
    return count

print(count_char(phrase, char_to_count))

# lambda count_char
l_count_char = lambda phrase, char_to_count: len( list(filter(lambda c: c == char_to_count.lower(), phrase.lower())) )
print(l_count_char(phrase, char_to_count))