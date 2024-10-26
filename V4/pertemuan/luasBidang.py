print("-----------------")
print("Luas Bidang")
print("-----------------")
print("Pilih Bidang:",
    "\n1. Segitiga",
    "\n2. Lingkaran",
    "\n3. Persegi Panjang")

pilihan = int(input("Masukkan pilihan: "))

#Segitiga
if (pilihan == 1):
    alas = eval(input("Masukkan alas: "))
    tinggi = eval(input("Masukkan tinggi: "))

    #hitung hasil
    hasil = alas * tinggi / 2
    print(f"Luas segitiga adalah: {hasil}")

#Lingkaran
elif(pilihan == 2):
    jari2 = eval(input("Masukkan jari-jari: "))

    #hitung hasil
    hasil = 3.14 * jari2 ** 2
    print(f"Luas lingkaran adalah: {hasil}")

#Persegi Panjang
elif(pilihan == 3):
    panjang = eval(input("Masukkan panjang: "))
    lebar = eval(input("Masukkan lebar: "))

    #hitung hasil
    hasil = panjang * lebar
    print(f"Luas Persegi Panjang adalah: {hasil}")

#Selain 1,2, dan 3
else:
    print("Pilihan tidak tersedia..")

#Penyampaian akhir
print("Terima kasih telah menggunakan program ini..")
