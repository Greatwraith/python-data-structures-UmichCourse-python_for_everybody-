# Kita bisa mendapatkan karakter tunggal apa pun dalam sebuah string
# menggunakan index yang ditentukan dalam tanda kurung siku.

# Index value itu integer. dimulai dari nol. 
# jadi karakter pertama memiliki index 0, 
# karakter kedua memiliki index 1, dan seterusnya.


# Contoh: Mengambil karakter dari string "Apple" menggunakan index.
fruit = "Apple"
# (A | P | P | L | E)
# (0 | 1 | 2 | 3 | 4)
print(fruit)

ambilHuruf = fruit[3] # Mengambil karakter pada index 3
print(ambilHuruf)  # Output: L



# Kita juga bisa menggunakan index untuk mengambil karakter terakhir
# dalam sebuah string dengan menggunakan index negatif.
x = 3
w = fruit[x-1]  # Mengambil karakter pada index 2 (x-1)
print(w)  # Output: P


# Mengambil karakter terakhir dengan index negatif
last_char = fruit[-1] # Mengambil karakter terakhir menggunakan index negatif (-1)
print(last_char)  # Output: E