import os.path
import datetime

f1 = input("Entrez le nom du premier fichier : ")
f2 = input("Entrez le nom du second fichier : ")

for fichier in [f1, f2]:
    if os.path.isfile(fichier):
        taille = os.path.getsize(fichier)
        modif = os.path.getmtime(fichier)
        date_modif = datetime.datetime.fromtimestamp(modif)
        print(f"Fichier {fichier} : {taille} octets, dernière modification le {date_modif}")
    else:
        print(f"Le fichier {fichier} n'existe pas.")

if os.path.isfile(f1) and os.path.isfile(f2):
    if os.path.getmtime(f1) > os.path.getmtime(f2):
        print(f"Le fichier le plus recent est : {f1}")
    elif os.path.getmtime(f1) < os.path.getmtime(f2):
        print(f"Le fichier le plus recent est : {f2}")
    else:
        print("Les deux fichiers ont la même date de modification.")
