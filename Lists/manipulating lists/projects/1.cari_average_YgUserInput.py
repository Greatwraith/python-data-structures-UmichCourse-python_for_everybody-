total = 0
count = 0 # set dulu menjadi kosong

while True:
    user_input = input("Enter a number: ") # user menginput beberapa numbers
    if user_input == "stop" : break # lalu user bilang stop
    value = float(user_input) # konversi input (string) jadi angka desimal
    
    total = total + value # tambahkan angka ke total keseluruhan
    count = count + 1 # hitung sudah berapa angka yang diinput

average = total / count # bagi total dengan jumlah angka
print("Average: {}".format(average)) # print average