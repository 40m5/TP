from functools import reduce

notes = [12, 15, 9, 18, 6, 20, 14]
conversion = [60.0, 75.0, 45.0, 90.0, 30.0, 100.0, 70.0]

convertir = map(lambda x: (x * 100) / 20, notes)
extraire = filter(lambda x: x>=50, conversion)
moyenne = reduce(lambda x, y: x / y, conversion)

print(list(convertir))
print(list(extraire))
print(moyenne)