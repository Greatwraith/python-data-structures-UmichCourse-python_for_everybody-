fruits = ['Banana', 'Apple', 'Orange', 'Mango', 'Grape', 'Watermelon', 'Pineapple']

# Banana | Apple | Orange | Mango | Grape | Watermelon | Pineapple
#   0    |   1   |    2   |    3  |   4   |     5      |     6


# 1.  Menghapus Item berdasarkan Index | remove('value item nya')
#    Hanya menghapus kemunculan pertama jika ada duplikat

fruits.remove('Apple')
fruits.remove('Orange')
newFruitsList = fruits
print("list baru, ada 2 yg diremove: {}\n".format(newFruitsList))




#2. Menghapus item berdasarkan nomor Indexnya 
#    pop() tanpa argumen → hapus item TERAKHIR
#    pop(index) → hapus item di index yang dimasukkan

# pop(salahSatuIndex)
pop_salahsatu = fruits.pop(0)
print('Setelah pop(1) : {}\n'.format(fruits))

# pop()
pop_itemTerakhir = fruits.pop()
print('Setelah pop() AKA pop item terakhir:  {}\n'.format(fruits))




#3.  menghapus items dari range index
#    kondisi list saat ini: ['Mango', 'Grape', 'Watermelon']
#                               0        1          2

del fruits[0:2]  # hapus index 0 dan 1 (Mango, Grape)
print(f'Setelah del fruits[0:2]      : {fruits}\n')
# Output: ['Watermelon']




#4.  Menghapus SEMUA item dalam list (clear)
#    list tetap ada, tapi isinya kosong []
fruits.clear()
print(f'Setelah clear()             : {fruits}\n\n')








#  CONTOH PROYEK

inventory = ['Sword', 'Shield', 'Potion', 'Bow', 'Arrow', 'Map', 'Key']
print(f'Inventory awal     : {inventory}')

# pakai potion (hapus berdasarkan nilai)
inventory.remove('Potion')
print(f'Setelah pakai Potion (remove)  : {inventory}')

# buang item terakhir (drop item)
dropped = inventory.pop()
print(f'Item yang di-drop (pop)        : {dropped}')
print(f'Inventory setelah drop         : {inventory}')

# hapus slot pertama (del)
del inventory[0]
print(f'Setelah del inventory[0]       : {inventory}')

# game over - kosongkan semua inventory
inventory.clear()
print(f'Game Over! Inventory sekarang  : {inventory}')
