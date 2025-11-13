import random

x = random.randint(0, 100)

compteur = 0

guess = int(input("Devinez le nombre mystère (entre 0 et 100) : "))

while guess != x:
    compteur += 1
    if guess < x:
        print("Plus haut !")
    else:
        print("Plus petit !")
    guess = int(input("Essayez encore : "))

compteur += 1
print("Bravo le nombre mystère était", x)
print("Vous l'avez trouvé en", compteur, "essais.")
