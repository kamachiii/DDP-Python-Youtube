# TASK:
# buatlah rumus menghitung luas persegi
# buatlah rumus menghitung luas persegi panjang
# buatlah rumus menghitung luas segitiga
# buatlah rumus menghitung luas lingkaran
# buatlah perbandingan  lebih besar dan lebih kecil dari luas persegi dan persegi panjang
# buatlah perbandingan lebih besar dan lebih kecil dari segitiga dan lingkaran

print("\n========== Luas Bangun Datar ==========\n\n")


# rumus luas persegi
sisi = 5
luasPersegi = sisi * sisi

print("---------- Luas Persegi ----------\n")
print(f"Luas Persegi dengan sisi {sisi} adalah {luasPersegi}")


# rumus luas persegi panjang
panjang = 10
lebar = 5
luasPersegiPanjang = panjang * lebar

print("\n\n---------- Luas Persegi Panjang ----------\n")
print(f"Luas Persegi Panjang dengan panjang {panjang} dan lebar {lebar} adalah {luasPersegiPanjang}")


# rumus luas segitiga
alas = 8
tinggi = 6
luasSegitiga = 0.5 * alas * tinggi

print("\n\n---------- Luas Segitiga ----------\n")
print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")


# rumus luas lingkaran
radius = 7
luasLingkaran = 3.14 * radius * radius

print("\n\n---------- Luas Lingkaran ----------\n")
print(f"Luas Lingkaran dengan jari-jari {radius} adalah {luasLingkaran}")


# perbandingan luas persegi dan persegi panjang
print("\n\n---------- Perbandingan Persegi dan Persegi Panjang ----------\n")

if luasPersegi > luasPersegiPanjang:
     print("Luas Persegi lebih besar dibandingkan Luas Persegi Panjang")
elif luasPersegi < luasPersegiPanjang:
     print("Luas Persegi lebih kecil dibandingkan Luas Persegi Panjang")
else:
     print("Luas Persegi sama dengan Luas Persegi Panjang")


# perbandingan luas segitiga dan lingkaran
print("\n\n---------- Perbandingan Segitiga dan Lingkaran ----------\n")
if luasSegitiga > luasLingkaran:
     print("Luas Segitiga lebih besar dibandingkan Luas Lingkaran")
elif luasSegitiga < luasLingkaran:
     print("Luas Segitiga lebih kecil dibandingkan Luas Lingkaran")
else:
     print("Luas Segitiga sama dengan Luas Lingkaran")

