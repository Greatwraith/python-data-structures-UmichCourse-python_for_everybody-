# list bisa di slice/dipotong
#  menggunakan :

t = [9 ,41, 12, 3, 74, 15]

# slice > from index number 1 then go on and stop before reacing index number 3
slice1 = t[1:3]
print(slice1)

# slice > from zero/the beginning then go on and stop before reaching index 4
slice2 = t[:4]
print(slice2)

# slice > from index 3 until the end
slice3 = t[3:]
print(slice3)

# slice > all of them
noSlice = t[:]
print(noSlice)

