chaine = input("Entrez un mot ou une phrase : ")

epuree = ""
for c in chaine.lower():
    if c.isalpha():
        epuree += c

if epuree == epuree[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
