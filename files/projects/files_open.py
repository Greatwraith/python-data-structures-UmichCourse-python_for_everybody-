# Membuka file dengan mode baca (read)

# handle = open('folder/filename', 'mode')
# mode: 'r' untuk membaca, 'w' untuk menulis, 'a' untuk menambahkan, 'x' untuk membuat file baru
# mode itu opsional, defaultnya adalah 'r' (read)


# Membuka file 'files/letter.txt' dengan mode baca | Jika file tidak ditemukan : FileNotFoundError
fhand = open('files/letter.txt', 'r')
print(fhand) # <open file 'files/letter.txt', mode 'r' at 0x7f8c8c8c8c8c>