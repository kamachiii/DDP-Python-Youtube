print("\n============ PT. XYZ ============")
while True:
    nama = input("\nNama Pegawai: ").capitalize() # capitalize() berfungsi untuk mengkapitalkan huruf pertama
    divisi = input("Divisi\t: ").capitalize()
    agama = input("Agama\t: ").capitalize() # lower() berfungsi untuk mengecilkan huruf
    jabatan = input("Jabatan\t: ").capitalize()

    # Gaji Pokok
    if jabatan == "Staff":
        gapok = 4000000
    elif jabatan == "Kabag":
        gapok = 7000000
    elif jabatan == "Manager":
        gapok = 10000000
    else:
        gapok = 0

    # Tunjangan Jabatan
    tunjab = int(gapok * 0.2)

    # Gaji Kotor
    gakot = int(gapok + tunjab)

    # Zakat Profesi
    zakat = int(gakot * 0.025) if agama == "Islam" and gakot >= 7000000 else 0

    # Gaji Bersih
    gaber = int(gakot - zakat)

    # Output
    print("\n============ DATA GAJI ============",
        f"\nNama\t\t: {nama}",
        f"\nAgama\t\t: {agama}",
        f"\nDivisi\t\t: {divisi}",
        f"\nJabatan\t\t: {jabatan}",
        f"\nGaji Pokok\t: {gapok:,}",
        f"\nTunjangan Jabatan: {tunjab:,}",
        f"\nGaji Kotor\t: {gakot:,}",
        f"\nZakat Profesi\t: {zakat:,}",
        f"\nGaji Bersih\t: {gaber:,}")

    ulang = input("\nIngin menginput lagi? (y/t): ").lower()
    if ulang != "y":
        break

print("Terima kasih telah menggunakan program ini.")
