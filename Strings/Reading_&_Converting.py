# Kami lebih memilih membaca data menggunakan string, 
# kemudian mengurai dan mengonversinya sesuai kebutuhan.

# Hal ini memberi kita kendali atas kesalahan input dari pengguna yang lalai.

# Angka yang diinput harus dikonversi dari string.


# Membaca nama dan usia dari pengguna sebagai string 
# dan kemudian mengonversi usia ke integer.
name = input("Masukkan nama Anda: ")
age = input("Masukkan usia Anda: ")

# Konversi usia dari string ke integer
age = int(age)
print(f"Halo, {name}! Anda berusia {age} tahun." + "\nIni adalah contoh konversi dari string ke integer.\n") 


# Contoh lain
# : Menghitung jumlah subsidi yang diberikan kepada seseorang berdasarkan jumlah awal yang mereka miliki.
subsidi = input("jumlah awal anda: ")
susidiDiberikan = 50000
rumus = "Perhitungannya = jumlah awal + subsidi yang diberikan"
tambah = int(subsidi) + susidiDiberikan

print("{} \nSubsidi yang diberikan: {}".format(rumus, tambah))



# Contoh float tentang menghitung luas lingkaran berdasarkan jari-jari yang diberikan oleh pengguna.
import math
radius = input("Masukkan radius jari-jari lingkaran: ")

# Konversi radius ke float untuk perhitungan luas lingkaran
area = math.pi * (float(radius) ** 2) 
# Luas lingkaran dihitung menggunakan rumus A = πr^2, di mana r adalah radius lingkaran.
# math.pi digunakan untuk mendapatkan nilai π, dan radius dikonversi ke float untuk memastikan perhitungan yang tepat.

 
print(f"Luas lingkaran dengan radius jari2 {radius} adalah: {area:.2f}")

