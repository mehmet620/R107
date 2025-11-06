x = int(input("Entrez x : "))
y = int(input("Entrez y : "))

print("Avant permutation:")
print(f"x : {x}")
print(f"y : {y}")

x, y = y, x

print("Après permutation:")
print(f"x : {x}")
print(f"y : {y}")
