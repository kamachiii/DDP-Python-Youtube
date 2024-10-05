angka1 = 25
"""
Skrip ini melakukan operasi aritmatika dasar pada dua angka dan mencetak hasilnya.
Variabel:
    angka1 (int): Angka pertama yang digunakan dalam operasi aritmatika.
    angka2 (int): Angka kedua yang digunakan dalam operasi aritmatika.
Operasi Aritmatika:
    penjumlahan (int): Hasil penjumlahan angka1 dan angka2.
    pengurangan (int): Hasil pengurangan angka2 dari angka1.
    perkalian (int): Hasil perkalian angka1 dengan angka2.
    pembagian (float): Hasil pembagian angka1 dengan angka2.
    modulus (int): Sisa hasil bagi angka1 dengan angka2.
    pangkat (int): Hasil pemangkatan angka1 dengan angka2.
    pembagian_bulat (int): Hasil pembagian bulat angka1 dengan angka2.
Output:
    Mencetak hasil operasi aritmatika dalam format string.
"""
angka2 = 2

# Melakukan operasi penjumlahan
penjumlahan = angka1 + angka2
# Melakukan operasi pengurangan
pengurangan = angka1 - angka2
# Melakukan operasi perkalian
perkalian = angka1 * angka2
# Melakukan operasi pembagian
pembagian = angka1 / angka2
# Menghitung sisa hasil bagi
modulus = angka1 % angka2
# Melakukan operasi pemangkatan
pangkat = angka1 ** angka2
# Melakukan operasi pembagian bulat
pembagian_bulat = angka1 // angka2

# Mencetak hasil penjumlahan
print(f"{angka1} + {angka2} = {penjumlahan}")
# Mencetak hasil pengurangan
print(f"{angka1} - {angka2} = {pengurangan}")
# Mencetak hasil perkalian
print(f"{angka1} * {angka2} = {perkalian}")
# Mencetak hasil pembagian
print(f"{angka1} / {angka2} = {pembagian}")
# Mencetak sisa hasil bagi
print(f"{angka1} % {angka2} = {modulus}")
# Mencetak hasil pemangkatan
print(f"{angka1} ** {angka2} = {pangkat}")
# Mencetak hasil pembagian bulat
print(f"{angka1} // {angka2} = {pembagian_bulat}")
