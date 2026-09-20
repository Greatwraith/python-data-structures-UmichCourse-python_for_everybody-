fruit = 'banana'

for letter in fruit:
    print(letter)
    
    
# For loop menelusuri setiap karakter dalam string secara langsung tanpa menggunakan index.
# Loop berhenti saat semua karakter dalam string telah diproses.




# Cara lain menggunakan while loop dengan index untuk menelusuri string:
# agak lebih panjang tapi memberikan kontrol lebih besar atas proses iterasi.
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1