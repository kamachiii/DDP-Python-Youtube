nama = "Tamuramaro Kamachi"
"""
Program ini menyimpan dan menampilkan data diri seseorang.
Variabel:
- nama: Menyimpan nama lengkap.
- nim: Menyimpan Nomor Induk Mahasiswa.
- tglLahir: Menyimpan tanggal lahir.
- jk: Menyimpan jenis kelamin.
- alamat: Menyimpan alamat tempat tinggal.
- kota: Menyimpan nama kota.
- prov: Menyimpan nama provinsi.
Fungsi:
- print(): Menampilkan data diri ke layar dengan format yang rapi menggunakan f-string.
"""
nim = "0110224094"
tglLahir = "23 Januari 2006"
jk = "Laki-laki"
alamat = "Jl. Veteran III No. 12A"
kota = "Bogor"
prov = "Jawa Barat"


print("\n========== Data Diri ==========\n")

# f sebelum kutip berfungsi untuk memformat string agar bisa menggunakan variabel didalam string
print(f"Nama\t\t: {nama}",
        f"\nNIM\t\t: {nim}",
        f"\nTanggal Lahir\t: {tglLahir}",
        f"\nJenis Kelamin\t: {jk}",
        f"\nAlamat\t\t:  {alamat}",
        f"\nKota\t\t: {kota}",
        f"\nProvinsi\t: {prov}")

print("\n========== Data Diri ==========\n")
