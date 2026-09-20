fhand = open("Lists/mbox-short.txt")

# Iterasi setiap baris dalam file
for line in fhand:
    line = line.rstrip()         # Hapus whitespace/newline di ujung kanan baris
    words = line.split()         # Pecah baris menjadi list kata-kata

    # Guardian pattern: lewati baris jika kosong ATAU kata pertama bukan 'From'
    # (baris pengirim selalu diawali 'From', bukan 'From:')
    if len(words) < 1 or words[0] != 'From':
        continue

    # words[2] adalah hari pengiriman (contoh: 'Sat', 'Fri', dst.)
    print(words[2])