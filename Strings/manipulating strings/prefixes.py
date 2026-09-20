# Prefixes adalah bagian awal dari sebuah string.
# Kita dapat memeriksa apakah sebuah string memiliki prefix tertentu 
# menggunakan metode `startswith()`. 



# Berikut adalah contoh penggunaannya:

line = 'Python is a great programming language.'

check = line.startswith('Python')
print(check)  # Output: True

check_p = line.startswith('p')
check_P = line.startswith('P')
print(check_p)  # Output: False, karena 'p' kecil tidak sama dengan 'P' besar
print(check_P)  # Output: True, karena 'P' besar adalah prefix dari string tersebut


# contoh menggunakan if statement untuk memeriksa prefix:
if line.startswith('Python'):
    print("The line starts with 'Python'.")
else:
    print("The line does not start with 'Python'.")
    
    
# kita juga bisa memeriksa prefix dengan menggunakan slicing untuk mengambil bagian awal string:

# 'ambil dari index 0 sampai index 5 (6 karakter pertama) untuk memeriksa prefix'
prefix = line[:6]  # Mengambil 6 karakter pertama dari string
print(prefix)  # Output: 'Python'