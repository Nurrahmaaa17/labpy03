max1 = 0
while True:
    angka = int(input("Masukan bilangan = "))
    if max1 < angka:
        max1 = angka
    if angka == 0:
        break
print("Bilangan Terbesarnya Adalah = ", angka)
