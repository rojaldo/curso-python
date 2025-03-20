calificaciones = [8.6, 7.8, 9.0, 8.7, 7.9, 8.1, 8.5, 9.1, 8.8, 8.9]

suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f'El promedio de las calificaciones es: {promedio}')

sorted = calificaciones.sort()
# reverse the list
sorted = calificaciones[::-1]

print(f'La calificación más alta es: {calificaciones[0]}')
print(f'La calificación más baja es: {calificaciones[-1]}')
print(f'Las calficacon 4 y 5 son: {calificaciones[3:5]}')