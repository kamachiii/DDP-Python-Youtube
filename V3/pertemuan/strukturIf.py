#belajar struktur kendali if
pelanggan = "Kamachiw"
total_belanja = 150000

#logika if jika belanja diatas atau sama dengan 100000 maka akan mendapatkan hadiah
if total_belanja >= 100000:
    ket = "Selamat anda mendapatkan hadiah\nTermiasih telah berbelanja"
else:
    ket = "Terima kasih telah berbelanja"

print(f"Hai, {pelanggan}!\n",
      f"Total belanja anda adalah Rp.{total_belanja}\n",
      f"{ket}")

