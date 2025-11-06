a = int(input("Entrez la premiere valeur : "))
b = int(input("Entrez la deuxieme valeur : "))
c = int(input("Entrez la troisieme valeur : "))

print(f"Les valeurs entrees sont : a = {a}, b = {b} et c = {c}")

temp = a
a = c
c = b
b = temp

print("Permutation: a ==> b, b ==> c, c ==> a")
print(f"Les valeurs permutees sont : a = {a}, b = {b} et c = {c}")
