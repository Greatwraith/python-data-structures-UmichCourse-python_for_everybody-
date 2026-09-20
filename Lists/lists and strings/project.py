# String berisi satu baris teks, mirip format log email
line = "From stephen.marquard@uct.ac.za Sat jan 5 09:14:!6 2026"
words = line.split()

# Mengambil elemen index ke-1 (kata kedua), yaitu alamat email lalu mencetaknya
email = words[1]
print("Email: {}".format(email))  

# Memecah email berdasarkan "@" sebagai delimiter
# → menghasilkan list berisi [username, domain]
pieces = email.split("@")
print("Email detail: {}".format(pieces))  # ['stephen.marquard', 'uct.ac.za']