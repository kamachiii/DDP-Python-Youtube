print("============ GAJI KARYAWAN ============")
while True:
    nama = input("Nama Karyawan: ")
    divisi = input("Divisi: ")
    agama = input("Agama: ")
    jabatan = input("Jabatan: ")

    if(jabatan == "staff"):
        gapok = 4000000
    elif(jabatan == "kabag"):
        gapok = 7000000
    elif(jabatan == "manager"):
        gapok = 10000000
    else:
        print("Data tidak ditemukan!")
        break;
    tunjab = gapok * 20 / 100
    gakot = gapok + tunjab
    zakat = gakot * 2.5 / 100 if agama == "muslim" and gapok >= 7 else 0
    gaber = (gapok + tunjab) - zakat

    gapok = f"Rp. {int(gapok):,}"
    tunjab = f"Rp. {int(tunjab):,}"
    gakot = f"Rp. {int(gakot):,}"
    zakat = f"Rp. {int(zakat):,}"
    gaber = f"Rp. {int(gaber):,}"

    print(f"Nama Karyawan\t\t: {nama}"
          f"\nAgama\t\t\t: {agama}"
          f"\nDivisi\t\t\t: {divisi}"
          f"\nJabatan\t\t\t: {jabatan}"
          f"\nGaji Pokok\t\t: {gapok}"
          f"\nTunjangan Jabatan\t: {tunjab}"
          f"\nGaji Kotor\t\t: {gakot}"
          f"\nZakat Profesi\t\t: {zakat}"
          f"\nGaji Bersih\t\t: {gaber}")
    ulang = input("Cek lagi (y/n)?")

    if ulang != "y":
        break;
