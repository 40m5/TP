age = [12, 25, 17, 18, 40, 15, 22]
vieux = [30, 15, 65, 74, 86, 98, 62]

adulte = filter(lambda x: x >= 18, age)
senior = filter(lambda x: x >= 60, vieux)

print(list(adulte))
print(list(senior))