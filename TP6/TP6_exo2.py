def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]
print("lst1 :", lst1)

lst2 = ajouter_elt(lst1, len(lst1))
print("lst2 :", lst2)

print("lst1 :", lst1, "type:", type(lst1), "id:", id(lst1))
print("lst2 :", lst2, "type:", type(lst2), "id:", id(lst2))
