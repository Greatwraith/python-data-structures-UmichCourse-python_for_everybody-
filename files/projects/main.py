# Program ini membaca isi sebuah file teks dan menampilkannya baris per baris.
# Jika file tidak ditemukan atau tidak bisa dibuka, program akan menampilkan pesan error.


# user input path file, contoh: files/letter.txt
fname = input("Enter the file name and its folder: ")

# Mencoba membuka file; jika gagal, tampilkan error lalu hentikan program
try:
    fhand = open(fname)
except:
    print('File cannot be opened: {} \nthe path or the file name are probably wrong'.format(fname))
    quit()

# cetak
for line in fhand:
    line = line.strip()
    print(line)


