# disini kita akan menggunakan functions/method yang fungsinya
# 1. mencari berapa banyak items di list
# 2. mencari yang nomor paling besar 
# 3. mencari yang nomor paling kecil
# 4. sum semua nomor/jumlahkan semua
# 5. mencari rata-rata

numbers = [3, 41, 12, 9, 88, 15]


print(len(numbers)) # cari len atau berapa banyak items di list | len(listnya..)

print(max(numbers)) # cari yang number paling besar | max(listnya..)

print(min(numbers)) # cari yang number paling kecil | min(listnya..)

print(sum(numbers)) # sum semua numbers | sum(listnya..)

print(sum(numbers)/len(numbers)) # mencari average/rata-rata | PERHITUNGAN



# 
print("\n")
# 




# cari len atau berapa banyak items di list 
checkLen = len(numbers)
print(checkLen)

# cari yang number paling besar 
largestNumber = max(numbers)
print(largestNumber)


# cari yang number paling kecil 
smallestNumber = min(numbers)
print(smallestNumber)

# sum semua numbers
sumAllNumbers = sum(numbers)
print(sumAllNumbers)

# mencari average/rata-rata
# hasil sum : isi list
average = sum(numbers)/len(numbers)
print(average)









