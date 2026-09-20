# Jika delimiter tidak ditentukan, spasi (termasuk spasi berulang)
# akan dianggap sebagai satu pemisah.
line_withSpaces = "A lot     of spaces"
SpacesToList = line_withSpaces.split()

print(SpacesToList)       # ['A', 'lot', 'of', 'spaces']
print(len(SpacesToList))  # 4




# Kita dapat menentukan karakter pemisah (delimiter) secara manual.
# Di contoh ini, underscore ("_") digunakan sebagai pemisah.
line_withUnderscores = "this_string_use_multiple_underscores"
UnderscoresToList = line_withUnderscores.split("_")

print(UnderscoresToList)       # ['this', 'string', 'use', 'multiple', 'underscores']
print(len(UnderscoresToList))  # 5