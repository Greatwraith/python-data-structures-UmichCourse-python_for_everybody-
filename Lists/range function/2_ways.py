friends = ['Joseph', 'Glenn', 'Robert', 'Damian', 'Victor']

# Cara 1 
# tinggal sebut nama listnya, Python otomatis ambil satu per satu isinya.
# Cocok kalau kamu cuma butuh nilainya saja tanpa peduli posisinya di mana.

# Cara 2 
# kamu iterasi angkanya dulu lewat `range`, baru pakai angka itu sebagai pintu masuk ke index list.
# Lebih panjang, tapi kamu pegang kendali penuh atas posisi setiap item
# berguna kalau butuh tahu "ini item ke berapa" atau mau akses dua item sekaligus berdasarkan posisi.

#  Cara 1 adalah default di Python — pakai Cara 2 hanya kalau memang butuh indexnya.



# CARA 1 — iterasi langsung
for my_friend in friends:
    print("Happy new year, {}!".format(my_friend))


print(" ")


# CARA 2 — iterasi via index
for i in range(len(friends)):
    friend = friends[i]
    print("Happy new year, {}!".format(friend))



# Menampilkan nomor urut
for i in range(len(friends)):
    print("{}. {}".format(i + 1, friends[i]))
# 1. Joseph
# 2. Glenn
# 3. Robert ...

# Bandingkan dengan item berikutnya
for i in range(len(friends) - 1):
    print("{} dan {} adalah teman".format(friends[i], friends[i+1]))