# Tipe data dan Variabel

## Tipe Data
Tipe data ada banyak, diantaranya:
* Integer (int) = untuk menyimpan bilangan bulat
* Floating point (float) = untuk menyimpan bilangan rill
* Complex number (complex) = untuk menyimpan bilangan kompleks
* String (str) = untuk menyimpan rangkaian karakter
* Boolean (bool) = untuk menyimpan nilai True (Benar) atau False (Salah)
* Collection/Sequence = menyimpan data yang kolektif/array, nanti list, tuple, dictionary, stack

## Operator Aritmatika
<table>
    <tr>
        <th>Operator</th>
        <th>Deskrisi</th>
        <th>Contoh</th>
        <th>Hasil</th>
    </tr>
    <tr>
        <td>+</td>
        <td>Perjumlahan</td>
        <td>x = y + 2</td>
        <td>x = 7</td>
    </tr>
    <tr>
        <td>-</td>
        <td>Pengurangan</td>
        <td>x = y - 2</td>
        <td>x = 3</td>
    </tr>
    <tr>
        <td>*</td>
        <td>Perkalian</td>
        <td>x = y * 2</td>
        <td>x = 10</td>
    </tr>
    <tr>
        <td>/</td>
        <td>Pembagian</td>
        <td>x = y / 2</td>
        <td>x = 2.5</td>
    </tr>
    <tr>
        <td>%</td>
        <td>Modulus/Sisa bagi</td>
        <td>x = y % 2</td>
        <td>x = 1</td>
    </tr>
</table>

> [!NOTE]
> ```y = 5```

## Operator Pembanding
<table>
    <tr>
        <th>Operator</th>
        <th>Deskrisi</th>
        <th>Contoh</th>
    </tr>
    <tr>
        <td>==</td>
        <td>Sama dengan</td>
        <td>x == 8 hasilnya False</td>
    </tr>
    <tr>
        <td>===</td>
        <td>Sama dengan (tipe datanya juga harus sama)</td>
        <td>
            x === 5 hasilnya True
            x === '5' hasilnya False
        </td>
    </tr>
    <tr>
        <td>!=</td>
        <td>Tidak sama dengan</td>
        <td>x != 8 hasilnya True</td>
    </tr>
    <tr>
        <td>></td>
        <td>Lebih besar</td>
        <td>x > 8 hasilnya False</td>
    </tr>
    <tr>
        <td><</td>
        <td>Lebih kecil</td>
        <td>x < 8 hasilnya true</td>
    </tr>
    <tr>
        <td>>=</td>
        <td>Lebih besar atau sama</td>
        <td>x >= 8 hasilnya False</td>
    </tr>
    <tr>
        <td><=</td>
        <td>Lebih kecil atau sama</td>
        <td>x <= 8 hasilnya True</td>
    </tr>
</table>

>[!NOTE]
> ```x = 5```

## Operator Pemberi Nilai
<table>
    <tr>
        <th>Operator</th>
        <th>Contoh</th>
        <th>Sama seperti</th>
        <th>Hasil</th>
    </tr>
    <tr>
        <td>=</td>
        <td>x = y</td>
        <td></td>
        <td>x = 5</td>
    </tr>
    <tr>
        <td>+=</td>
        <td>x += y</td>
        <td>x = x + y</td>
        <td>x = 15</td>
    </tr>
    <tr>
        <td>-=</td>
        <td>x -= y</td>
        <td>x = x - y</td>
        <td>x = 5</td>
    </tr>
    <tr>
        <td>*=</td>
        <td>x *= y</td>
        <td>x = x * y</td>
        <td>x = 50</td>
    </tr>
    <tr>
        <td>/=</td>
        <td>x /= y</td>
        <td>x = x / y</td>
        <td>x = 2</td>
    </tr>
    <tr>
        <td>%=</td>
        <td>x %= y</td>
        <td>x = x % y</td>
        <td>x = 0</td>
    </tr>
</table>

> [!NOTE]
> ```x = 10```
> ```y = 5```

## Operator Logika
<table>
    <tr>
        <th>Operator</th>
        <th>Deskrisi</th>
        <th>Contoh</th>
    </tr>
    <tr>
        <td>&&</td>
        <td>Dan</td>
        <td>(x < 10 && y > 1) hasilnya True</td>
    </tr>
    <tr>
        <td>||</td>
        <td>Atau</td>
        <td>(x == 5 || y == 5) hasilnya False</td>
    </tr>
    <tr>
        <td>!</td>
        <td>Bukan/Pembalik</td>
        <td>!(x==y) hasilnya True</td>
    </tr>
</table>

> [!NOTE]
> ```x = 10```
> ```y = 7```

## Variabel
Variabel adalah hasil pembacaan suatu tipe data yang disimpan. Untuk menyimpannya kita menggunakan Operator Pemberi Nilai "=". Untuk menghubungkan string ```""``` atau ```''``` dengan variabel menggunakan ```,```. Jika ingin memberikan line baru, maka menggunakan ```\n``` dan jika ingin menggunakan ```tab``` maka gunakan ```\t```. Variable yang bagus adalah menggunakan huruf kecil dan tidak boleh diawali dengan angka serta tidak boleh menggunakan spasi. Penulisan variabe memiliki aturan-aturan seperti berikut:

1. Karakter pertama harus berupa huruf atau _underscore_ ```_```
2. Karakter selanjutnya dapat berupa huruf, _underscore_, atau angka
3. Karakter pada nama variabel bersifat sensitif (_sensitive case_), artinya huruf kecil dan huruf besar dibedakan. Sebagai contoh, variabel ```namaDepan``` dan ```namadepan``` adalah variabel yang berbeda.

```python
# Contoh
nama = "nama"
namaAyah = "nama ayah"
nama_ibu = "nama ibu"
```

Cara mengecek sebuah tipe data dari sebuah variabel menggunakan "type()"

```python
# Contoh
nama = "nama"
namaAyah = "nama ayah"
nama_ibu = "nama ibu"
```
