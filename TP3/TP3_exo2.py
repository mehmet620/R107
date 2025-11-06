#version avec for

import time

n = int(input("Entrez un nombre entier positif : "))

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)

#version avec while

import time

n = int(input("Entrez un nombre entier positif : "))

while n >= 0:
    print(n)
    time.sleep(1)
    n -= 1
