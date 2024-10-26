#belajar struktu kendali if dengan operator logika
siswa = "Osama bin Laden"
nilai = 55

''' ini bentuk komentar multiline
logika lulus minimal 60
if nilai >= 60:
    ket = "Lulus"
else:
    ket = "Tidak Lulus"
'''

#ternary operator
ket = "Lulus" if nilai >= 60 else "Tidak Lulus"

print(f" Nama:\t\t {siswa}\n",
        f"Nilai:\t\t {nilai}\n",
        f"Keterangan:\t {ket}")

if nilai >= 85:
    predikat = "A 👑"
elif nilai >= 75:
    predikat = "B 💰"
elif nilai >= 65:
    predikat = "C 🦖"
else:
    predikat = "D ✈💥🏢🏢🔥"

print(f"Predikat:\t {predikat}")
