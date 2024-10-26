print("============ LUAS BIDANG ============")

luas_list = []

while True:
  print("\n============ Pilih rumus ============")
  print(" 1. Persegi\n",
      "2. Persegi Panjang\n",
      "3. Segitiga\n",
      "4. Lingkaran\n",
      "0. Exit")

  rumus = int(input("Pilih rumus: "))

  print()

  if rumus == 1:
    sisi = int(input("Masukkan sisi: "))

    keliling = sisi * 4
    luas = sisi ** 2
    luas_list.append(luas)

    print(f"Dik:\tsisi = {sisi}\n",
        "Dit:\tK = ?\n",
        "\tL = ?\n",
        f"Dij:\tK = 4 × s\n",
        f"\t   = 4 × {sisi}\n",
        f"\t   = {keliling} \n \n",
        f"\tL = s × s\n",
        f"\t   = {sisi} x {sisi}\n",
        f"\t   = {luas}")

  elif rumus == 2:
    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))

    keliling = (panjang + lebar) * 2
    luas = panjang * lebar
    luas_list.append(luas)

    print(f"Dik:\tpanjang = {panjang}\n",
        f"\tlebar = {lebar}\n",
        "Dit:\tK = ?\n",
        "\tL = ?\n",
        f"Dij:\tK = 2 × (p + l)\n",
        f"\t   = 2 × ({panjang} + {lebar})\n",
        f"\t   = 2 × {panjang + lebar}\n",
        f"\t   = {keliling} \n \n",
        f"\tL = p × l\n",
        f"\t   = {panjang} × {lebar}\n",
        f"\t   = {luas}")

  elif rumus == 3:
    alas = int(input("Masukkan alas/a: "))
    tinggi = int(input("Masukkan tinggi/b: "))
    c = input("Masukkan c: ")

    keliling = alas + tinggi + int(c)
    luas = (alas * tinggi) / 2
    luas_list.append(luas)

    print(f"Dik:\talas = {alas}\n",
        f"\ttinggi = {tinggi}\n",
        "Dit:\tK = ?\n",
        "\tL = ?\n",
        f"Dij:\tK = a + b + c\n",
        f"\t   = {alas} + {tinggi} + {c}\n",
        f"\t   = {keliling} \n \n",
        f"\tL = (a × t) ÷ 2\n",
        f"\t   = ({alas} × {tinggi}) ÷ 2\n",
        f"\t   = {alas * tinggi} ÷ 2\n",
        f"\t   = {luas}")

  elif rumus == 4:
    jari2 = int(input("Masukkan jari-jari: "))
    phi = 3.14
    keliling = 2 * phi * jari2
    luas = phi * jari2 ** 2
    luas_list.append(luas)

    print(f"Dik:\tjari² = {jari2}\n",
        f"\tphi = {phi}\n",
        "Dit:\tK = ?\n",
        "\tL = ?\n",
        f"Dij:\tK = 2 × π × r\n",
        f"\t   = 2 × {phi} × {jari2}\n",
        f"\t   = {keliling} \n \n",
        f"\tL = π × r²\n",
        f"\t   = {phi} x {jari2}²\n",
        f"\t   = {luas}")

  elif rumus == 0:
    break

  else:
    print("Pilihan tidak ada...")

  if len(luas_list) > 1:
    print("\nPerbandingan hasil luas:")
    for i in range(len(luas_list)):
      for j in range(i + 1, len(luas_list)):
        print(f"Luas {i+1} ({luas_list[i]}) vs Luas {j+1} ({luas_list[j]}): {luas_list[i] - luas_list[j]}")

