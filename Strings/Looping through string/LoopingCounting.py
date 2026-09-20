# looping dan counting karakter dalam string 
# Looping digunakan untuk menelusuri setiap karakter dalam string, 
# sedangkan counting digunakan untuk menghitung jumlah kemunculan karakter tertentu dalam string.

word = 'Watermelon'

count = 0

for letter in word:
    if letter == 'e':
        count += 1
print(count)