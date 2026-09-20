# Menghitung jumlah baris dalam file

# kita menggunakan fungsi open() untuk membuka file dengan mode "r" (read) untuk membaca isi file.
# Setelah itu, kita menggunakan for loop untuk membaca setiap baris/lines dalam file lalu mencetaknya.

fhand = open("files/letter.txt", "r")
count = 0

for line in fhand:
    count += 1
    print("Line Count:", count, line)
    
# buka file dengan mode "r" (read)
# inisialisasi variabel count untuk menghitung jumlah baris dalam file
# gunakan for loop untuk membaca setiap baris dalam file dan mencetaknya dengan nomor baris.
