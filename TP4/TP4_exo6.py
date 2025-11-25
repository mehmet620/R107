tab = [5, 2, 4, 8, 1, 3]

print(tab)

for i in range(len(tab)):
    min_index = i
    for j in range(i+1, len(tab)):
        if tab[j] < tab[min_index]:
            min_index = j
    tab[i], tab[min_index] = tab[min_index], tab[i]
    print(tab)

#sorted(tab)
tab = [5, 2, 4, 8, 1, 3]
print(sorted(tab))
print(tab)

#tab,sort()
tab = [5, 2, 4, 8, 1, 3]
tab.sort()
print(tab)
