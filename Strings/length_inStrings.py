# fungsi Len() digunakan untuk menghitung jumlah karakter dalam sebuah string,
# namun bukan index value. ‼️
# Fungsi ini menghitung semua karakter dalam string.

fruit = "Apple"

# panjang string "Apple" adalah 5.
# karena ada 5 karakter dalam string tersebut, yaitu A, P, P, L, dan E.

# tetapi index value dari  "Apple" dimulai dari 0, jadi karakter terakhir memiliki index 4.
# (A | P | P | L | E)
# (0 | 1 | 2 | 3 | 4)


fruitLength = len(fruit)  # Menghitung jumlah karakter dalam string "Apple"
print(f"Jumlah karakter dalam string '{fruit}' \nadalah: {fruitLength}")


