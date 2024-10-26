pelanggan = "Jamal al Ghitani"
total = 1000000

ket = "Selamat, dapat diskon 1 poin 🦖" if total >= 500000 else "Terima kasih atas pembelian Anda"

print("Nama Pelanggan:\t", pelanggan,
      "\nTotal Belanja:\t", total,
      "\n", ket)
