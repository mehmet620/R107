n = int(input("Entrez un nombre entier: "))

if n > 0:
    if n % 2 == 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")
elif n < 0:
    if n % 2 == 0:
        print("Le nombre est négatif et pair")
    else:
        print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro (et il est pair)")
