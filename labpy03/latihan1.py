import random

n = int(input('Masukan Nilai N: '))

for i in range(n):
    angka = random.uniform(.0, .5)
    print("data ke-", i, ":", angka)
