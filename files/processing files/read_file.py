# kita bisa menggunakan fungsi open() untuk membuka file dengan mode "r" (read) untuk membaca isi file.
# Setelah itu, kita bisa menggunakan for loop untuk membaca setiap baris dalam file dan mencetaknya.

# membuka file dengan mode "r" (read)
xfile = open("files/letter.txt", "r")

# membaca setiap baris dalam file dan mencetaknya
for line in xfile:
    print(line)