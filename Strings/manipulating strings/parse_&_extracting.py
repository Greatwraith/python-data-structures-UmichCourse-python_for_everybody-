# Parse dan extracting ini bertujuan untuk mengambil host/domain dari email


# 
data = 'From Stephen.marquard@(uct.ac.za) Sat Jan 5 09:14:16 2008'

# mencari posisi karakter '@' dalam string data
atpos = data.find('@') # mencari posisi karakter '@' dalam string data untuk menentukan awal host/domain
print(atpos) # output: 21, karena karakter '@' berada pada index ke-21 dalam string data

# mencari posisi karakter spasi setelah karakter '@' dalam string data
sppos = data.find(' ', atpos) # mencari spasi setelah posisi '@' untuk memastikan kita mendapatkan host/domain yang benar
print(sppos) # output: 31, karena karakter spasi setelah '@' berada pada index ke-31 dalam string data

# mengambil substring dari string data
# yang dimulai dari karakter setelah '@' hingga karakter sebelum spasi
host = data[atpos+1 : sppos] # slicing untuk mengambil bagian host/domain dari email
print(host) # output: 'uct.ac.za', karena itu adalah substring yang berada di antara '@' dan spasi dalam string data