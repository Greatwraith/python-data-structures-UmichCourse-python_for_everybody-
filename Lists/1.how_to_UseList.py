fruits = ['Banana', 'Apple', 'Orange', 'Mango', 'Grape']


# Banana | Apple | Orange | Mango | Grape
#   0    |   1   |    2   |    3  |   4         


#1.  menambah/append item ke list | append(...)
fruits.append('watermelon')
print(f'{fruits}\n')


#2.  Memasukkan item ke nomor index spesifik | insert(indexNumber, 'isinya')
fruits.insert(1, 'pineapple')
print(f'{fruits}\n')


#3.  menambah banyak items ke list | extend('itembaruPertama', 'itembaruKeDua')
new_fruits_fromIndo = ['Durian', 'Papaya']
fruits.extend(new_fruits_fromIndo)
print(f'{fruits}\n')


#4.  Memodifikasi list | variable[indexNumber] = 'isi dengan item baru/modifikasi'
modified_something = fruits[1] = 'Avocado'
print('sucesfully Modified an item in the list!'.format(modified_something))
print(f'{fruits}\n\n')



# CONTOH PROYEK

new_fruits = ['kiwi', 'lime']
combined_list = fruits + new_fruits
# di dalam variabel combined_list = buah-buahan diawal + buah buahan baru 

print(f"Combine list: {combined_list}")
print(f"Original list after : {fruits}")