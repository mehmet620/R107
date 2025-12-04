chaine = input("Entrez une phrase : ")

taille = 0
for c in chaine:
    taille += 1
print(f"Taille de la chaine : {taille}")

voyelles = "aeiouy"
nb_voyelles = 0
for c in chaine.lower():
    if c in voyelles:
        nb_voyelles += 1
pourcentage = (nb_voyelles / taille) * 100
print(f"Pourcentage de voyelles : {pourcentage:.2f}%")

mot = "wagon"
pos = -1
for i in range(taille - len(mot) + 1):
    if chaine[i:i+len(mot)].lower() == mot:
        pos = i
        break
if pos != -1:
    print(f"La sous-chaine 'wagon' commence a la position {pos}")
else:
    print("La sous-chaine 'wagon' n'existe pas")

occurrences = 0
for i in range(taille - len(mot) + 1):
    if chaine[i:i+len(mot)].lower() == mot:
        occurrences += 1
print(f"Le mot 'wagon' apparait {occurrences} fois")
