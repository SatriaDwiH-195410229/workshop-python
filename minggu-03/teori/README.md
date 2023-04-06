# 5. STRUKTUR DATA
Bab ini berisi tentang penjelasan beberapa materi yang sebelumnya sudah kita pelajari, tetapi dengan lebih detail dan juga ada beberapa tambahan materi.

## 5.1. List: Tambahan
List memiliki beberapa method. Berikut method-method milik objek list:
- list.**append**_(x)_ = berguna untuk menambahkan sebuah item pada akhir list. Setara dengan `a[len(a):] = [x]`.
- list.**extend**_(iterable)_ = memperbesar list dengan cara menambahkan seluruh item dari _iterable_ (objek yang memiliki iterator). Setara dengan `a[len(a):] = iterable`
- list.**insert**_(i, x)_ = memasukkan item pada posisi yang sudah ditentukan. Argumen pertama adalah index dari elemen yang akan dimasukkan sebelumnya. Jadi, `a.insert(0, x)` masuk pada sisi paling depan sebuah list, dan `a.insert(len(a), x)` setara dengan `a.append(x)`.
- list.**remove**_(x)_ = menghapus item pertama pada sebuah list. Item yang dihapus adalah item yang nilainya adalah `x`. Jika tidak ada item tersebut, maka akan muncul [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError).
- list.**pop**_([i])_ = menghapus item pada posisi tertentu pada sebuah list, dan di-return. Jika tidak ada indeks yang ditetapkan, maka `a.pop()` menghapus dan me-return item terakhir dalam list.
- list.**clear**_()_ = menghapus semua item pada list. Setara dengan `del a[:]`.
- list.**index**_(x[, start[, end]])_ = me-return _zero-based index_ pada list item pertama yang nilainya sama dengan `x`. Jika tidak ada item tersebut maka akan muncul [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError).
- list.**count**_(x)_ = me-return jumlah berapa kali `x` muncul dalam list.
- list.**sort**_(, key=None, reverse=False)_ = mengurutkan item pada sebuah list dengan _ascending_ atau _descending_ (defaultnya adalah _ascending_). Untuk penjelasan lebih lanjut tentang sort bisa lihat di [sorted](https://docs.python.org/3/library/functions.html#sorted).
- list.**reverse**_()_ = memutar balik elemen yang ada pada sebuah list.
- list.**copy**_()_ = me-return _shallow copy_ (salinan) list. Setara dengan `a[:]`

Berikut contoh penggunaan method list:
```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4) # mencari banana dimulai dari posisi 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
Bisa kita perhatikan jika method-method yang hanya memodifikasi list seperti `insert`, `remove`, atau `sort` tidak menampilkan _return value_. Method-method tersebut me-return nilai default yaitu `None`. Hal ini merupakan prinsip desain seluruh struktur data _mutable_ (data yang elemennya bisa diubah) pada Python.

Selain itu, bisa juga kita perhatikan bahwa tidak semua data bisa di-sort (diurutkan) atau dibandingkan. Contohnya, `[None, 'hello', 10]` tidak bisa diurutkan karena integer tidak dapat dibandingkan dengan string. `None` juga tidak dapat dibandingkan dengan tipe data lain.

### 5.1.1. Menggunakan List sebagai Stack ###
Method-method list dapat mempermudah dalam menggunakan list sebagai stack (tumpukan), yaitu elemen terakhir yang ditambahkan merupakan elemen pertama yang diterima (LIFO / last-in first-out). Untuk menambahkan sebuah item di atas stack, kita bisa gunakan `append()`. Untuk mengambil sebuah item dari atas stack, kita bisa gunakan `pop()` tanpa index eksplisit. Contoh:
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
- - - - - - -
### 5.1.2. Menggunakan List sebagai Queue ###
Kita juga bisa menggunakan list sebagai queue (antrian), yaitu elemen pertama yang ditambahkan merupakan elemen pertama yang diterima (FIFO / first-in, first-out). Walaupun begitu, penerapan queue ini tidak efisien untuk list. Kenapa? Karena _append_ dan _pop_ dari akhir list akan berjalan dengan cepat, sementara melakukan _insert_ dan _pop_ dari awal list akan berjalan dengan lambat. 

Untuk menerapkan queue, kita bisa gunakan [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) yang didesain untuk melakukan proses _append_ dan _pop_ dengan cepat dari sisi manapun. Contoh:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") # Terry masuk
>>> queue.append("Graham") # Graham masuk
>>> queue.popleft() # Pertama masuk sekarang keluar
'Eric'
>>> queue.popleft() # Kedua masuk sekarang keluar
'John'
>>> queue # Sisa antrian yang diurutkan berdasarkan kedatangan
deque(['Michael', 'Terry', 'Graham'])
```
- - - - - - -
### 5.1.3. List Comprehensions ###
_List comprehensions_ menyediakan cara yang singkat dan efisien dalam membuat list. List comprehension biasanya digunakan untuk membuat list baru dari elemen-elemen list yang sudah ada. Dengan list comprehension, kita bisa membuat loop dengan lebih jelas dan kita bisa membuat list secara otomatis dalam satu _command line_ saja.

Misalnya adalah ketika kita ingin membuat list berisi hasil kuadrat:
```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Bisa kita perhatikan bahwa pembuatan list tersebut menghasilkan sebuah variabel bernama x yang masih ada ketika loop selesai. Kita juga bisa menghitung list tersebut dengan menggunakan cara ini:
```python
squares = list(map(lambda x: x**2, range(10)))
```
atau:
```python
squares = [x**2 for x in range(10)]
```
- - - - - - - -
List comprehension terdiri dari _bracket_ yang berisi sebuah expresi yang diikuti dengan klausa `for`, lalu dilanjut dengan klausa `for` atau `if` bernilai nol atau lebih. Hasilnya adalah sebuah list baru yang dihasilkan dari perhitungan expresi tersebut. Contohnya adalah saat listcomp (list comprehension) menggabungkan dua elemen dari dua list jika kedua elemen tersebut tidak sama:
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
sepadan dengan:
```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
- - - - - - -
Jika ekspresi berupa tuple, maka kita perlu parentheses (diletakkan di dalam kurung):
```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # buat list baru yang nilainya dikali dua
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # melakukan filter pada list untuk meniadakan angka negatif
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # terapkan fungsi ke semua elemen
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # panggil method pada setiap elemen
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # buat list 2-tuples seperti (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # tuple harus di-parenthesized, jika tidak maka akan muncul error.
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # memaparkan list menggunakan listcomp dengan dua 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
- - - - - - -
List comprehensions juga dapat berisi ekspresi yang kompleks dan fungsi _nested_:
```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```
- - - - - 
### 5.1.4. Nested List Comprehensions ###
Expresi pertama pada sebuah list comprehension bisa berupa ekspresi arbitrary (ekspresi yang dipilih/digunakan sesuai dengan keinginan personal user), atau juga bisa berupa list comprehension lain.

Contoh berikut adalah matriks 4x4 yang diimplementasikan sebagai 3 list yang masing-masing memiliki length 4:
```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
List comprehension berikut mengubah urutan baris dan kolom:
```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Seperti yang kita lihat pada _section_ sebelumnya, _nested listcomp_ dievaluasi di dalam konteks for yang mengikuti _nested listcomp_. Jadi contoh tersebut sama dengan:
```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
yang juga sama dengan:
```python
>>> transposed = []
>>> for i in range(4):
...     # 3 baris di bawah digunakan untuk implementasi nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Kita harus menggunakan fungsi built-in untuk statement flow yang kompleks. Kita bisa menggunakan fungsi [zip()](https://docs.python.org/3/library/functions.html#zip) :
```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## 5.2. Statement `del`
Statement `del` berguna untuk menghapus item dari list pada index yang ditentukan. `del` berbeda dari `pop()` yang me-return nilai. Statement `del` juga bisa digunakan untuk menghapus [slice](https://www.w3schools.com/python/ref_func_slice.asp) dari sebuah list atau juga bisa menghapus seluruh isi list. Contoh:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```
[del](https://docs.python.org/3/reference/simple_stmts.html#del) juga bisa digunakan untuk menghapus seluruh variabel:
```python
del a
```
## 5.3. Tuple dan Sequence
List dan string memiliki properti yang mirip seperti operasi _indexing_ dan _slicing_. Karena Python merupakan bahasa pemrograman yang masih terus berevolusi, maka selalu ada kemungkinan untuk menambahkan tipe data sequence baru. Python juga memiliki tipe data sequence standar bernama _tuple_.

Tuple berisi kumpulan nilai yang dipisah dengan koma, contoh:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuple bisa berbentuk nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuple bersifat immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # Tuple bisa berisi objek mutable:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```
Bisa kita perhatikan jika output tuple pasti ditampilkan di dalam parentheses (tanda kurung), sehingga _nested tuples_ bisa diinterpretasikan dengan benar oleh Python.

Walaupun tuple mirip dengan list, seringkali tuple digunakan pada situasi berbeda dan juga untuk tujuan yang berbeda pula. Tuple bersifat [immutable](https://docs.python.org/3/glossary.html#term-immutable) dan memiliki elemen yang heterogen. Semantara List bersifat [mutable](https://docs.python.org/3/glossary.html#term-mutable) dan memiliki elemen yang homogen.

Tuple empty (kosong) dibentuk oleh sepasang parentheses yang kosong. Tuple dengan satu item dibentuk oleh sebuah value yang diikuti dengan koma. Contoh:
```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
Statement `t = 12345, 54321, 'hello!'` adalah contoh dari [tuple packing](https://levelup.gitconnected.com/improve-your-python-coding-tuple-packing-and-unpacking-44bd92daab31). Value `12345`, `54321`, dan `hello!` dikemas bersama di dalam sebuah tuple. 

Kita juga bisa melakukan operasi yang merupakan kebalikan dari _tuple packing_. Contoh:
```Python
>>> x, y, z = t
```
Kode di atas bisa kita sebut dengan _sequence unpacking_. _Sequence unpacking_ dapat mengambil objek dari sebuah _collection_ dan meletakkannya di variabel untuk digunakan pada suatu saat nanti.

## 5.4. Sets
Set adalah sebuah koleksi tidak urut yang tidak memiliki elemen yang diduplikat. Dengan kata lain, set adalah sebuah tipe data kolektif yang bisa digunakan untuk menyimpan nilai dalam satu variabel dengan satu ketentuan yaitu nilai yang disimpan harus berbeda dari yang lain (unik).

Kurung kurawal atau fungsi `set()` bisa digunakan untuk membuat berbagai set. Untuk membuat empty set, kita harus menggunakan `set()`, bukan `{}`. 

Berikut contoh demonstrasi penggunaan set:

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket) # menunjukkan jika duplikat sudah dihapus
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrasi operasi set pada huruf untuk dari dua kata
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a # huruf unik di a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b # huruf di a tapi tidak di b
{'r', 'd', 'b'}
>>> a | b # huruf di a atau b atau di keduanya
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b # huruf di a dan b
{'a', 'c'}
>>> a ^ b # huruf di a atau b tapi tidak di keduanya
{'r', 'd', 'b', 'm', 'z', 'l'}
```
mirip seperti list comprehension, set comprehension juga disupport:
```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```
## 5.5. Dictionaries
Dictionary adalah tipe data pada python yang berfungsi untuk menyimpan kumpulan nilai (value) dengan _key-value_. Dictionary pada bahasa pemrograman lain biasanya berupa array asosiatif. Tidak seperti sequence yang diindex dengan range angka, dictionary diindex dengan _key_ bersifat _immutable_ bertipe string atau angka. Tuple bisa digunakan sebagai key jika tuple tersebut hanya berisi string, angka, dan tuple. Jika tuple tersebut berisi berisi objek _mutable_ baik secara langsung maupun tidak langsung, tuple tersebut tidak bisa digunakan sebagai key dictionary. Kita tidak bisa menggunakan list sebagai key karena list bisa dimodifikasi langsung menggunakan _index assignments_, _slice assignments_, ataupun dengan method seperti `append()` dan `extend()`.

Operasi utama pada dictionary adalah memasukkan value dengan key lalu meng-ekstrak value berdasarkan key. Pada dictionary, penggunaan `list(d)` akan me-return sebuah list berisi seluruh key yang digunakan di dalam dictionary. Untuk memeriksa apakah sebuah key ada di dalam dictionary, kita bisa gunakan keyword [in](https://docs.python.org/3/reference/expressions.html#in).

Berikut contoh penggunaan dictionary:
```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
Konstruktor [dict()](https://docs.python.org/3/library/stdtypes.html#dict) menciptakan dictionaries langsung dari sequence key-value pairs:
```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
dict comprehension dapat digunakan untuk menciptakan dictionary dari key arbitrary dan expresi value:
```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
Jika key berbentuk string sederhana, maka kita akan lebih mudah dalam menetapkan _pairs_ menggunakan argumen keyword:
```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
## 5.6. Teknik Looping
Ketika melakukan looping melewati dictionary, key dan _corresponding value_ dapat didapatkan pada waktu yang sama menggunakan method `item()`:
```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```
- - - - - -
Ketika looping melewati sequence, index dan _corresponding value_ bisa didapatkan pada waktu bersamaan menggunakan fungsi [enumerate()](https://docs.python.org/3/library/functions.html#enumerate).

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
- - - - - - -
Untuk melakukan loop pada dua atau lebih sequence pada waktu yang sama, _entries_ dapat dipasangkan dengan fungsi [zip()](https://docs.python.org/3/library/functions.html#zip).

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
- - - - - - -
Untuk melakukan loop pada sequence secara terbalik, pertama kita harus menetapkan sequence ke arah maju kemudian panggil fungsi [reversed()](https://docs.python.org/3/library/functions.html#reversed).
```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
- - - - - - - -
Untuk melakukan loop pada sequence secara urut, gunakan fungsi [sorted()](https://docs.python.org/3/library/functions.html#sorted) yang me-return sebuah list baru yang elemennya urut tanpa mengubah apapun pada list lama.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```
- - - - - - -
Menggunakan [set](https://docs.python.org/3/library/stdtypes.html#set) pada sebuah sequence dapat menghapus elemen duplikat. Kombinasi sorted() dan set() pada sebuah sequence merupakan cara idiomatis untuk melakukan loop pada elemen unik milik sequence secara urut.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```
- - - - - - -
Kadangkala kita ingin mengganti list pada saat kita melakukan loop. Walau begitu, sebenarnya lebih mudah dan lebih aman jika kita membuat list baru.
```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```
## 5.7. Kondisi: Tambahan
Kondisi yang digunakan di statement `while` dan `if` dapat berisi segala operator, tidak hanya perbandingan.

Operator perbandingan `in` dan `not in` adalah _membership tests_ yang menentukan apakah nilai ada di dalam kontainer atau tidak. Operator `is` dan `is not` membandingkan apakah dua objek merupakan objek yang sama.

Perbandingan dapat diikat (digabung). Misalnya, `a < b == c`. Perbandingan juga dapat dikombinasikan menggunakan operator Boolean yaitu `and` dan `or`, dan hasil dari perbandingan tersebut bisa dinegasikan dengan `not`.

Kita bisa menempatkan hasil dari perbandingan atau expresi Boolean lain ke dalam sebuah variabel. Contoh:
```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```
## 5.8. Membandingkan Sequence dan Tipe Lain
Objek sequence biasanya dibandingkan dengan objek lain yang memiliki tipe sequence sama. Pembanding menggunakan urutan _lexicographical_: pertama, dua item pertama dibandingkan. Jika dua item tersebut berbeda maka hal ini dapat menentukan hasil dari perbandingan. Jika dua item setara, maka dua item selanjutnya dibandingkan. Begitu terus hingga sequence selesai. 

Urutan _lexicographical_ untuk string menggunakan angka unicode point untuk mengurutkan karakter individual. Contoh perbandingan antara sequence yang memiliki tipe sama:
```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
Bisa kita perhatikan bahwa membandingkan objek dengan tipe berbeda dengan `< or >` diperbolehkan, asalkan objek memiliki metode perbandingan yang sesuai. Contohnya, tipe numerik campuran dapat dibandingkan menurut nilai numeriknya, misalnya `0` sama dengan `0.0`.
