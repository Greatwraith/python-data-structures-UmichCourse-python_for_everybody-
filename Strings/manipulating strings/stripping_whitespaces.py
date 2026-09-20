word = '  Hello, World!  '

removeBothSides = word.strip() # menghapus whitespace di kedua sisi
removeOnlyLeft = word.lstrip() # menghapus whitespace di sebelah kiri
removeOnlyRight = word.rstrip() # menghapus whitespace di sebelah kanan


print(word, '\n')

print(removeBothSides)
print(removeOnlyLeft)
print(removeOnlyRight)
