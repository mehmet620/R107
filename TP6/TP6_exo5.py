import unicodedata

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = ''.join(ch for ch in texte if ch.isalnum())
    return texte

def supprimer_accents(texte):
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(ch for ch in texte if unicodedata.category(ch) != 'Mn')
    return texte

def est_palindrome(texte):
    texte = nettoyer_texte(texte)
    texte = supprimer_accents(texte)
    return texte == texte[::-1]

def main():
    phrase = input("Entrez un mot ou une phrase : ")
    if est_palindrome(phrase):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()
