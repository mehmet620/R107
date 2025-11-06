
debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or fin < 0 or debut > 24 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
elif debut > fin:
    print("Attention ! le début de la location est après la fin ...")
else:
    tarif1 = 0
    tarif2 = 0

    for h in range(debut, fin):
        if (h >= 0 and h < 7) or (h >= 17 and h < 24):
            tarif1 += 1
        else:
            tarif2 += 1

    print("Vous avez loué votre vélo pendant")
    if tarif1 > 0:
        print(f"{tarif1} heure(s) au tarif horaire de 1.0 euro(s)")
    if tarif2 > 0:
        print(f"{tarif2} heure(s) au tarif horaire de 2.0 euro(s)")

    total = tarif1 * 1.0 + tarif2 * 2.0
    print(f"Le montant total à payer est de {total:.1f} euro(s).")
