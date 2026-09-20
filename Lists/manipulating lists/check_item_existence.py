# cek apakah suatu item benar berada di list tersebut.
# output TRUE artinya ada
# output FALSE artinya tidak ada

electronics = ['Fridge', 'Air conditioning', 'Microwave', 'Rice cooker', 'Coffe maker']

# menggunakan in untuk cek, apakah suatu item benar berada di List
# ADA
checkFridge = 'Fridge' in electronics
print(checkFridge) # output : True

# ADA
checkAC = 'Air conditioning'in electronics
print(checkAC) # output : True



# Item gak ada di list | FALSE
FalseCheck = 'Television' in electronics
print(FalseCheck) # output : FALSE

# Kalau ada typo atau kelebihan spasi akan False | tidak terdeteksi | FALSE
typoCheck = 'Microwave ' in electronics # ada spasi lebihan sehabis micorwave | Microwave..
print(typoCheck) # output : FALSE

# salah satu huruf salah kapitalnya, seharusnya dimulai dengan huruf besar | FALSE
wrongUpperLowerCase = 'microwave' in electronics  
print(wrongUpperLowerCase) # output : FALSE


