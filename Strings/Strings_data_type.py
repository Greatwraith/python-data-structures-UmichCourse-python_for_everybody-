# String adalah serangkaian karakter huruf.
# string literal menggunakan tanda kutip 'Halo dunia' / "halo dunia"

# ( + ) + di python berarti menggabungkan string

# ketika string berisi angka '12345' maka itu tetap dianggap string,
# bukan angka integer, karena masih berada di dalam tanda kutip.

# kita bisa mengubah karakter strinG menjadi angka integer atau float
# dengan fungsi int() atau float()

# kita bisa mengubah angka integer atau float menjadi string dengan fungsi str()



# contoh penggunaan string dan concatenation

string1= "Halo"
string2= 'dari Python'
gabungkan = string1 + " " + string2
print(gabungkan)


# contoh mengubah string menjadi angka integer fungsi int()
angka1 = '1234' # angka1 string berada di dalam tanda kutip > ubah ke integer
angka2 = 67890
ubahKeINTEGER = int(angka1) + angka2
print(ubahKeINTEGER)


# contoh mengubah string menjadi angka float fungsi float()
angka3 = '3.14' # angka3 string berada di dalam tanda kutip > ubah ke float
angka4 = 2.71828
ubahKeFLOAT = float(angka3) + angka4
print(ubahKeFLOAT)


# contoh mengubah angka integer atau float menjadi string dengan fungsi str()

angka5 = 100 # angka5 integer berada di luar tanda kutip > ubah ke string
angka6 = 3.14159 # angka6 float berada di luar tanda kutip > ubah ke string

ubahKeSTRING1 = str(angka5) + " adalah angka integer"
ubahKeSTRING2 = str(angka6) + " adalah angka float"
print(ubahKeSTRING1)
print(ubahKeSTRING2)
