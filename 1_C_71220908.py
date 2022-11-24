print("========== Pilih Menu ==========")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
   
angka1 = int(input("Masukkan angka pertama:"))
angka2 = int(input("Masukkan angka kedua:"))
pilih = input("Pilihan Anda:")
if pilih == "1":
    penjumlahan= angka1 + angka2
    print(penjumlahan)
elif pilih == "2":
    pengurangan= angka1 - angka2
    print(pengurangan)
elif pilih == "3":
    perkalian= angka1 * angka2
    print(perkalian)
elif pilih == "4":
    pembagian= angka1 / angka2
    print(pembagian)

