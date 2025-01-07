from functools import reduce

ventes = [120, 50, 30, 20, 90, 100]
total = reduce (lambda x, y: x + y, ventes)
produit = reduce (lambda x, y: x * y, ventes)

print(total)
print(produit)