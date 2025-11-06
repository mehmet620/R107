a = int(input("Entrez la premiere valeur : "))
b = int(input("Entrez la deuxieme valeur : "))
c = int(input("Entrez la troisieme valeur : "))
print(f"Les valeurs entrees sont : a = {a}, b = {b} et c = {c}")

a, b, c = c, a, b

print("Permutation: a ==> b, b ==> c, c ==> a")
print(f"Les valeurs permutees sont : a = {a}, b = {b} et c = {c}")
