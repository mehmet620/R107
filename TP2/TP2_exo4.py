BASE = 4

Fromage = 800.0
Eau = 2.0
Ail = 2.0
Pain = 400.0

NbrConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

Fromage = Fromage * NbrConvives / BASE
Eau = Eau * NbrConvives / BASE
Ail = Ail * NbrConvives / BASE
Pain = Pain * NbrConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {NbrConvives} personnes, il vous faut :")
print(f"- {Fromage:.1f} gr de fromage")
print(f"- {Eau:.1f} dl d'eau")
print(f"- {Ail:.1f} gousse(s) d'ail")
print(f"- {Pain:.1f} gr de pain")
