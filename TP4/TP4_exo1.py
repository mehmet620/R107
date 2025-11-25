x = float(input("Vous cherchez la table de multiplicationn de quel nombre ? :  "))

table = []

for i in range(10):
    produit = round(x * i, 1)
    table.append(produit)

for i in range(10):
    print(f"{x} * {i} = {table[i]}")

