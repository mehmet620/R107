minutes = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))

jour = minutes // (24 * 60) + 1

print("La date associée est le jour", jour, "du mois.")