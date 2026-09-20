# Fungsi range mengembalikan daftar angka yang berkisar dari nol hingga satu kurang dari parameter.

friends = ['Joseph', 'Glenn', 'Robert', 'Damian', 'Victor']



# --- Cara Python (langsung iterasi list) ---
for friend in friends:
    print(friend)

print(" ")




# --- Cara lama (pakai range + index) ---
for i in range(len(friends)):
    print(i, friends[i])
    
print(" ")  
  
  
  
    
# --- range(start, stop) ---
# mulai dari index 1, berhenti sebelum index 5 
for i in range(0, 5):
    print(i, friends[i])
    
print(" ")




# --- range(start, stop, step) ---
# lompat 2 index setiap iterasi
for i in range(0, len(friends), 2):
    print(i, friends[i])