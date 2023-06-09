vec = [-4, -2, 0, 2, 4]

# buat list baru yang nilainya dikali dua
print([x*2 for x in vec])

# melakukan filter pada list untuk meniadakan angka negatif
print([x for x in vec if x >= 0])

# terapkan fungsi ke semua elemen
print([abs(x) for x in vec])

# panggil method pada setiap elemen
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# buat list 2-tuples seperti (number, square)
print([(x, x**2) for x in range(6)])

# tuple harus di-parenthesized, jika tidak maka akan muncul error.
# ---kcontoh kode error, hapus '#' untuk mencoba kode error---
# print([x, x**2 for x in range(6)])
# --- contoh kode error, hapus '#' untuk mencoba kode error---

# memaparkan list menggunakan listcomp dengan dua 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])