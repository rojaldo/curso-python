# Ejercicio 6: Dada la cadena "aprendiendo python", imprime el primer y último carácter de la cadena. Luego, imprime cada palabra en la cadena y la primera y última letra de cada palabra.
phrase = 'aprendiendo, python'
print(f'El primer carater es: {phrase[0]}; el último es: {phrase[-1]}')
# save eahc word in a list
words = phrase.split()

for word in words:
    print(word)
    print(f'La primera letra de la palabra es: {word[0]}; la última es: {word[-1]}')

# Ejercicio 7: Dada la cadena "Programación en Python", usa slicing para extraer la palabra "Python" y guárdala en una nueva variable

phrase = 'Programación en Python'
word_to_extract = 'Python2' 
words = phrase.split()

# new_word = ''
for word in words:
    if word == word_to_extract:
        new_word = word
    else:
        new_word = '<No se encontró la palabra>'
print(new_word)