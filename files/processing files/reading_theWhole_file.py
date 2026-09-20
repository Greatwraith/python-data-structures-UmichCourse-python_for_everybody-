# Kita dapat menggunakan metode read() untuk membaca seluruh isi file ke dalam satu string.

fhand = open("files/letter.txt", "r")
inp = fhand.read()

print(len(inp)) # mencetak seluruh jumlah karakter dalam string yang berisi isi file.

print(inp[:20])  # mencetak 20 karakter pertama dari string yang berisi isi file.



# Kita dapat membaca seluruh file (termasuk baris baru) ke dalam satu string.

# gunakan fungsi open() untuk membuka file dengan mode "r" (read) untuk membaca isi file.
# Setelah itu, gunakan metode read() untuk membaca seluruh isi file ke dalam satu string.
# Kemudian, gunakan fungsi len() untuk menghitung jumlah karakter dalam string tersebut & mencetakannya.



