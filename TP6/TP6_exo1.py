L1 = [0] * 3
print("Liste :", L1)
print("Type :", type(L1))
print("ID :", id(L1))

for i, elt in enumerate(L1):
    print(f"Élément {i} : valeur={elt}, type={type(elt)}, id={id(elt)}")

L1[1] += 1
print("Nouvelle liste :", L1)
print("Type :", type(L1))
print("ID :", id(L1))

for i, elt in enumerate(L1):
    print(f"Élément {i} : valeur={elt}, id={id(elt)}")

ch = "chaine"
print("Chaîne :", ch, "ID :", id(ch))

for i, c in enumerate(ch):
    print(f"Caractère {i} : '{c}', type={type(c)}, id={id(c)}")
