#a)
N = int(input("Entrez N : "))
somme = 0
for i in range(N+1):   # de 0 à N inclus
    somme += i
print("La somme des entiers de 0 à", N, "est :", somme)
#b)
val = 0
while val != 100:
    val = int(input("Entrez une valeur (100 pour arrêter) : "))
print("Fin de la boucle, vous avez saisi 100.")
#c)
inf10 = 0
entre10et15 = 0
sup15 = 0

for i in range(10):
    val = float(input(f"Entrez la valeur {i + 1} (entre 0 et 20) : "))
    while val < 0 or val > 20:
        val = float(input("Valeur incorrecte, entrez une valeur entre 0 et 20 : "))

    if val < 10:
        inf10 += 1
    elif val < 15:
        entre10et15 += 1
    else:
        sup15 += 1

print("Nombre de valeurs < 10 :", inf10)
print("Nombre de valeurs >= 10 et < 15 :", entre10et15)
print("Nombre de valeurs >= 15 :", sup15)
#d)
X = int(input("Entrez un nombre supérieur à 1 : "))
somme = 0
N = 0

while somme + N <= X:
    somme += N
    N += 1

print("Le plus grand N tel que la somme <= X est :", N-1)
