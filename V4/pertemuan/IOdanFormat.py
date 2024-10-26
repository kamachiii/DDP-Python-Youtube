#belajar IO dan Format print()
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

hasil = angka1 * angka2

print(angka1, "x", angka2, "=", hasil)
print("%f * %f = %f" % (angka1, angka2, hasil))
