notes = []
coeffs = []

for i in range(5):
    entree = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    valeur = entree.split(" ")
    note = float(valeur[0])
    coeff = int(valeur[1])
    notes.append(note)
    coeffs.append(coeff)

somme_notes = 0
somme_coeffs = 0
for i in range(5):
    somme_notes += notes[i] * coeffs[i]
    somme_coeffs += coeffs[i]

moyenne = somme_notes / somme_coeffs

admis = moyenne > 10 and all(note >= 8 for note in notes)

print(f"La moyenne generale est : {moyenne}")
if admis:
    print("L'etudiant est admis")
else:
    print("L'etudiant n'est pas admis")
