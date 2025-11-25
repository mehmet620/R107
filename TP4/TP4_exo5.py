date = input("Entrez une date au format jjmmaaaa : ")


if len(date) != 8 or not date.isdigit():
    print("Format incorrect ! La date doit être au format jjmmaaaa (8 chiffres).")
else:

    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:8])


    if mois < 1 or mois > 12:
        print("Date incorrecte : le mois doit être compris entre 01 et 12.")
    else:

        if mois in [1, 3, 5, 7, 8, 10, 12]:
            jours_max = 31
        elif mois in [4, 6, 9, 11]:
            jours_max = 30
        elif mois == 2:

            if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
                jours_max = 29
            else:
                jours_max = 28

        if jour < 1 or jour > jours_max:
            print("Date incorrecte : le jour n'existe pas pour ce mois/année.")
        else:
            print("Date correcte :", f"{jour:02d}/{mois:02d}/{annee}")
