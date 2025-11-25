L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

max_occurrences = 0
element_frequent = L[0]

for i in range(len(L)):
    compteur = 0
    for j in range(len(L)):
        if L[i] == L[j]:
            compteur += 1
    if compteur > max_occurrences:
        max_occurrences = compteur
        element_frequent = L[i]

print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({max_occurrences} x)")







L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

max_occurrences = 0
element_frequent = L[0]

for x in L:
    compteur = L.count(x)
    if compteur > max_occurrences:
        max_occurrences = compteur
        element_frequent = x

print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({max_occurrences} x)")
L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

max_occurrences = 0
element_frequent = L[0]

for x in L:
    compteur = L.count(x)
    if compteur > max_occurrences:
        max_occurrences = compteur
        element_frequent = x

print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({max_occurrences} x)")
