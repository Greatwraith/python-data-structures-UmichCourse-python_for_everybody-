# Program untuk mencari dan mencetak baris yang mengandung kata "kata berbentuk string" 
# dari file "letter.txt"

fhand = open("files/letter.txt", "r")

for line in fhand:
    line = line.strip() #menghapus karakter whitespace di awal dan akhir line
    if not 'Dear' in line: # jika line tidak mengandung "Dear", lanjutkan ke iterasi berikutnya
        continue #melanjutkan ke iterasi berikutnya jika kondisi tidak terpenuhi
    print(line) # hanya akan dieksekusi jika line mengandung "Dear"
    
    
# line = line.strip()   -＞  menghapus karakter whitespace di awal dan akhir line
# if not 'Dear' in line: continue   -＞  jika line tidak mengandung "Dear", lanjutkan ke iterasi berikutnya
# print(line)   -＞  hanya akan dieksekusi jika line mengandung "Dear"

# outputnya adalah semua baris yang mengandung kata "Dear" dari file "letter.txt"