nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
total= 0.0
notes = []

for i in range(nombreEtudiants) :
    note = float(input(f"Note etudiant {i+1} : "))
    while note < 0 or note > 20 :
        note = float(input(f"Note etudiant {i + 1} : "))
    notes.append(note)
    total += note
moyenne = round(total / nombreEtudiants, 2)

print(f"Moyenne de classe : {moyenne}")
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = round(notes[i]-moyenne , 2 )
    print(f"{i} | {notes[i]} | {ecart}")

