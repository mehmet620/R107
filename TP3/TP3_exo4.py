n = int(input("Entrez un entier positif : "))
choix = input("Choisissez la boucle (for/while) : ")

fact = 1

if choix == "for":
    for i in range(1, n+1):
        fact *= i
        print(f"Après multiplication par {i}, la factorielle vaut {fact}")
elif choix == "while":
    i = 1
    while i <= n:
        fact *= i
        print(f"Après multiplication par {i}, la factorielle vaut {fact}")
        i += 1
else:
    print("Choix invalide .")
