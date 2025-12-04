somme = int(input("Entrez une somme en euros : "))

billets100 = somme // 100
reste = somme % 100

billets50 = reste // 50
reste = reste % 50

billets10 = reste // 10
reste = reste % 10

pieces2 = reste // 2
reste = reste % 2

pieces1 = reste

print(f"{somme} euros, c'est donc {billets100} billets de 100, {billets50} de 50, {billets10} de 10, {pieces2} pieces de 2 et {pieces1} piece 1.")
