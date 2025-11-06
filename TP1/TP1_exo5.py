jour = int(input("Entrez le jour du mois : "))
heure = int(input("Entrez l'heure (0-23) : "))
minute = int(input("Entrez les minutes (0-59) : "))

minutesTotales = (jour - 1) * 24 * 60 + heure * 60 + minute

print("Depuis le début du mois,", minutesTotales, "minutes se sont écoulées.")