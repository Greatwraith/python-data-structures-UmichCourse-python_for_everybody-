numlist = list() # buat list kosong untuk menyimpan angka-angka

while True:
    user_input = input("Enter a number: ") # user menginput beberapa numbers
    if user_input == "stop" : break # lalu user bilang stop
    value = float(user_input) # konversi input (string) jadi angka desimal
    numlist.append(value) # masukkan angka ke dalam list


average = sum(numlist) / len(numlist) # jumlah semua elemen dibagi banyaknya elemen
print("Average: {}".format(average)) # print average