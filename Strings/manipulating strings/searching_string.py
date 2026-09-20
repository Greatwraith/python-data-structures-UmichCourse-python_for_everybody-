fruit = 'banana'

# Menggunakan metode find() untuk mencari posisi pertama dari substring 'ban' dalam string fruit.
# Jika substring ditemukan, find() akan mengembalikan indeks posisi pertama dari substring tersebut.
# Jika substring tidak ditemukan, find() akan mengembalikan -1.

FindBAN = fruit.find('ban')
print(FindBAN) 
# output: 0, karena 'ban' ditemukan mulai dari indeks 0 dalam string 'banana'.
# b | a | n | a | n | a
# 0 | ......

findNA = fruit.find('na')
print(findNA)
# output: 2, karena 'na' ditemukan mulai dari indeks 2 dalam string 'banana'.
#  b | a | n | a | n | a
#  0 | 1 | 2 | ....