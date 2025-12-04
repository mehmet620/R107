nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

personne1 = f"{prenom1.capitalize()} {nom1.upper()}"
personne2 = f"{prenom2.capitalize()} {nom2.upper()}"

liste = [personne1, personne2]
liste.sort()

for p in liste:
    print(p)
