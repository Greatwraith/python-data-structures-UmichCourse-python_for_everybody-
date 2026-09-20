# Membuat List dari awal, yang isinya gak ada sama sekali/kosong. 
# lalu kita isi List yang kosong dengan Elements menggunakan beberapa method.

# list backpack kosong, gak ada isinya
backpack = list()

# menambah dengan Append | element baru akan berada di akhir karena itu eleman yang terbaru
backpack.append('Laptop')
print(backpack)

# menambah dengan extend | menambah multiple elements dalam waktu bersamaan
device_for_study = ['Mouse', 'TWS', 'Charger', 'Connector', 'Ipad']
backpack.extend(device_for_study)
print(backpack)