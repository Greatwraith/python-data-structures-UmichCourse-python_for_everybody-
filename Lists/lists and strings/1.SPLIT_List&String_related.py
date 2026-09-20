# LIST DAN STRING SALING TERHUBUNG

# Mendefinisikan variabel string
stringVariable = "coding this from my home"

# .split() memecah string berdasarkan spasi (default),
# lalu menyimpan setiap kata sebagai elemen terpisah dalam list baru.
toListVar = stringVariable.split()
# Contoh transformasi:
#   string → "coding this from my home"
#   list   → ['coding', 'this', 'from', 'my', 'home']


print(toListVar)        # menampilkan isi list hasil konversi
print(len(toListVar))   # len() menghitung jumlah elemen di dalam list

print("\n")

# menampilkan setiap elemen di toListVar beserta nomornya
count = 0
for element in toListVar:
    count += 1
    print("{}. {}".format(count, element))