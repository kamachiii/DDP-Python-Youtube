nama = input("Masukkan nama anda: ")
bb = float(input("Masukkan berat badan anda (kg): "))
tb = float(input("Masukkan tinggi badan anda (cm): "))
imt = bb / ((tb/100)**2)

if(imt < 18.5):
    ket = "Tulang Lab IPA"
elif(imt < 25):
    ket = "MC ANIMEK"
elif(imt < 30):
    ket = "VILLAIN"
else:
    ket = "PEJABAT"
print("Nama Mahasiswa:\t\t%s"
    "\nBerat badan:\t\t%.2f kg"
    "\nTinggi badan:\t\t%.2f cm"
    "\nIndeks massa tubuh:\t%.2f"
    "\nKeterangan:\t\t%s" %(nama, bb, tb, imt, ket))
