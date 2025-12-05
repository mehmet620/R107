import random

def generer(n, vmin, vmax):
    """Génère une liste de n valeurs aléatoires entre vmin et vmax inclus."""
    valeurs = [random.randint(vmin, vmax) for _ in range(n)]
    return valeurs

def combienInferieur(liste, seuil):
    """Retourne le nombre de valeurs de la liste inférieures au seuil."""
    compteur = sum(1 for val in liste if val < seuil)
    return compteur

def main():
    n = int(input("Combien de valeurs voulez-vous générer ? "))

    vmin = int(input("Valeur minimale (vmin) : "))
    vmax = int(input("Valeur maximale (vmax) : "))

    reponse = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ").strip().lower()
    if reponse in ['oui', 'o']:
        seuil = int(input("Précisez le seuil : "))
    else:
        seuil = 30

    valeurs = generer(n, vmin, vmax)
    print("Valeurs générées :", valeurs)

    nb_inferieur = combienInferieur(valeurs, seuil)
    print(f"Nombre de valeurs inférieures à {seuil} :", nb_inferieur)

if __name__ == "__main__":
    main()
