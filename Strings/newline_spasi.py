# kita menggunakan special character \n untuk membuat new line (baris baru)
# ibarat kita menekan tombol enter pada keyboard untuk membuat baris baru

# contoh penggunaan \n untuk membuat new line
say ='Hello \nWorld'
print(say)


# newline masih dianggap sebagai satu karakter, jadi kita bisa menggunakan len() untuk menghitungnya
xy = 'X\nY'
print(len(xy)) # 3