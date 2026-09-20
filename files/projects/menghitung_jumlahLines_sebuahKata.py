# Program ini menghitung jumlah baris yang diawali "Subject:" dalam sebuah file.
# Cara pakai: masukkan path file saat diminta, contoh: files/letter.txt

fname = input("Masukkan nama file dan foldernya: ")
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1

print("Ada {} baris Subject: di {}".format(count, fname))