heures = int(input("Entrez le nombre d'heures travaillees : "))
taux = float(input("Entrez le salaire horaire : "))

if heures <= 160:
    salaire = heures * taux
elif heures <= 200:
    salaire = (160 * taux) + (heures - 160) * (taux * 1.25)
else:
    salaire = (160 * taux) + (40 * taux * 1.25) + (heures - 200) * (taux * 1.5)

print(f"Le salaire de l'ouvrier est : {salaire} euros")
