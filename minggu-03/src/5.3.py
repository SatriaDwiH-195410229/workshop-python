t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuple bisa berbentuk nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuple bersifat immutable:
# ---contoh kode error, hilangkan '#' untuk mencoba kode error---
# t[0] = 88888
# ---contoh kode error, hilangkan '#' untuk mencoba kode error---

# Tuple bisa berisi objek mutable:
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello',    # <-- perhatikan koma
print(len(empty))
print(len(singleton))
print(singleton)

x, y, z = t