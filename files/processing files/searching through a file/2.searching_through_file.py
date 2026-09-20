# mencari melalui sebuah file

# membuka file "letter.txt" dalam mode baca
# 
# membaca file baris per baris dan mencari baris yang dimulai dengan "Subject:"
# jika line tidak dimulai dengan "Subject:", lanjutkan ke iterasi berikutnya
# 
# jika ditemukan, tampilkan baris tersebut


fhand = open("files/letter.txt")

# kita bisa menggunakan continue statement untuk melewati iterasi tertentu dalam loop
for line in fhand:
    line = line.strip()
    if not line.startswith("Subject:"): # jika line tidak dimulai dengan "Subject:", lanjutkan ke iterasi berikutnya
        continue #melanjutkan ke iterasi berikutnya jika kondisi tidak terpenuhi
    print(line) # hanya akan dieksekusi jika line dimulai dengan "Subject:"