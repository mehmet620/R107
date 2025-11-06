import random

x = random.randint(0, 100)

compteur = 0

guess = int(input("Devinez le nombre mystère (entre 0 et 100) : "))

while guess != x:
    compteur += 1
    if guess < x:
        print("Trop petit !")
    else:
        print("Trop grand !")
    guess = int(input("Essayez encore : "))

compteur += 1
print("Bravo ! Le nombre mystère était", x)
print("Vous l'avez trouvé en", compteur, "essai(s).")
