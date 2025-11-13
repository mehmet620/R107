nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []
somme = 0.0

for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:
        note = float(input(f"Note invalide. Recommencez pour l'étudiant {i} : "))
    notes.append(note)
    somme += note

moyenne = round(somme / nombreEtudiants, 2)
print(f"Moyenne de classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = round(notes[i] - moyenne, 2)
    print(f"{i} | {notes[i]} | {ecart}")
