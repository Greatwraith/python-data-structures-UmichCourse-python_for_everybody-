# mencari melalui sebuah file


# membuka file "letter.txt" dalam mode baca
# membaca file baris per baris dan mencari baris yang dimulai dengan "Subject:"
# jika ditemukan, tampilkan baris tersebut

fhand = open("files/letter.txt", "r")

for line in fhand:
    line = line.strip() #menghapus karakter whitespace di awal dan akhir line
    
    #cek apakah line dimulai dengan "Subject:" 
    # jika ya, tampilkan line tersebut
    if line.startswith("Subject:"):
        print(line) 
        
# kita bisa meletakan if statement di dalam loop for
# untuk hanya mengeksekusi kode tertentu ketika kondisi tertentu terpenuhi



