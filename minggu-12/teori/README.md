# Jupyter

Install jupyter terlebih dahulu dengan perintah berikut:

```python
conda install -c anaconda jupyter
```

Buka jupyter notebook:

```python
jupyter notebook
```

## STRUKTUR DATA

### 5.1. Lebih Banyak tentang List

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
In [1]: banana', 'kiwi', 'apple', 'banana']
        fruits.count('apple')
Out[1]: 2
In [2]: fruits.count('tangerine')
Out[2]: 0
In [3]: fruits.index('banana')
Out[3]: 3
In [4]: fruits.index('banana', 4) # mencari banana dimulai dari posisi 4
Out[4]: 6
In [5]: fruits.reverse()
        fruits
Out[5]: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
In [6]: fruits.append('grape')
        fruits
Out[6]: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
In [7]: fruits.sort()
        fruits
Out[7]: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
In [8]: fruits.pop()
Out[8]: 'pear'
```
Bisa kita perhatikan jika method-method yang hanya memodifikasi list seperti `insert`, `remove`, atau `sort` tidak menampilkan _return value_. Method-method tersebut me-return nilai default yaitu `None`. Hal ini merupakan prinsip desain seluruh struktur data _mutable_ (data yang elemennya bisa diubah) pada Python.

Selain itu, bisa juga kita perhatikan bahwa tidak semua data bisa di-sort (diurutkan) atau dibandingkan. Contohnya, `[None, 'hello', 10]` tidak bisa diurutkan karena integer tidak dapat dibandingkan dengan string. `None` juga tidak dapat dibandingkan dengan tipe data lain.

#### 5.1.1. Menggunakan List sebagai Stack
Method-method list dapat mempermudah dalam menggunakan list sebagai stack (tumpukan), yaitu elemen terakhir yang ditambahkan merupakan elemen pertama yang diterima (LIFO / last-in first-out). Untuk menambahkan sebuah item di atas stack, kita bisa gunakan `append()`. Untuk mengambil sebuah item dari atas stack, kita bisa gunakan `pop()` tanpa index eksplisit. Contoh:

```python
In [1]: stack = [3, 4, 5]
        stack.append(6)
        stack.append(7)
        stack
Out[1]: [3, 4, 5, 6, 7]
In [2]: stack.pop()
Out[2]: 7
In [3]: stack
Out[3]: [3, 4, 5, 6]
In [4]: stack.pop()
Out[4]: 6
In [5]: stack.pop()
Out[5]: 5
In [6]: stack
Out[6]: [3, 4]
```
#### 5.1.2. Menggunakan List sebagai Queue
Kita juga bisa menggunakan list sebagai queue (antrian), yaitu elemen pertama yang ditambahkan merupakan elemen pertama yang diterima (FIFO / first-in, first-out). Walaupun begitu, penerapan queue ini tidak efisien untuk list. Kenapa? Karena _append_ dan _pop_ dari akhir list akan berjalan dengan cepat, sementara melakukan _insert_ dan _pop_ dari awal list akan berjalan dengan lambat.

Untuk menerapkan queue, kita bisa gunakan [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) yang didesain untuk melakukan proses _append_ dan _pop_ dengan cepat dari sisi manapun. Contoh:

```python
In [1]: from collections import deque
        queue = deque(["Eric", "John", "Michael"])
        queue.append("Terry") # Terry arrives
        queue.append("Graham") # Graham arrives
        queue.popleft() # The first to arrive now leaves
Out[1]: 'Eric'
In [2]: queue.popleft() # The second to arrive now leaves
Out[2]: 'John'
In [3]: queue # Remaining queue in order of arrival
Out[3]: deque(['Michael', 'Terry', 'Graham'])
```
#### 5.1.3. List Comprehensions
_List comprehensions_ menyediakan cara yang singkat dan efisien dalam membuat list. List comprehension biasanya digunakan untuk membuat list baru dari elemen-elemen list yang sudah ada. Dengan list comprehension, kita bisa membuat loop dengan lebih jelas dan kita bisa membuat list secara otomatis dalam satu _command line_ saja.

Misalnya adalah ketika kita ingin membuat list berisi hasil kuadrat:

```python
In [1]: squares = []
        for x in range(10):
            squares.append(x**2)

        squares
Out[1]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Bisa kita perhatikan bahwa pembuatan list tersebut menghasilkan sebuah variabel bernama x yang masih ada ketika loop selesai. Kita juga bisa menghitung list tersebut dengan menggunakan cara ini:

```python
In [2]: squares = list(map(lambda x: x**2, range(10))) 
```
atau:
```python
In [3]: squares = [x**2 for x in range(10)]
```
List comprehension terdiri dari _bracket_ yang berisi sebuah expresi yang diikuti dengan klausa `for`, lalu dilanjut dengan klausa `for` atau `if` bernilai nol atau lebih. Hasilnya adalah sebuah list baru yang dihasilkan dari perhitungan expresi tersebut. Contohnya adalah saat listcomp (list comprehension) menggabungkan dua elemen dari dua list jika kedua elemen tersebut tidak sama:

```python
In [4]: [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
Out[4]: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
sepadan dengan:

```python
In [5]: combs = []
        for x in [1,2,3]:
            for y in [3,1,4]:
                if x != y:
                    combs.append((x, y))

        combs
Out[5]: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
Jika ekspresi berupa tuple, maka kita perlu parentheses (diletakkan di dalam kurung):

```python
In [6]: vec = [-4, -2, 0, 2, 4]
        # create a new list with the values doubled
        [x*2 for x in vec]
Out[6]: [-8, -4, 0, 4, 8]
In [7]: # filter the list to exclude negative  numbers
        [x for x in vec if x >= 0]
Out[7]: [0, 2, 4]
In [8]: # apply a function to all the elements
        [abs(x) for x in vec]
Out[8]: [4, 2, 0, 2, 4]
In [9]: # call a method on each element
        freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
        [weapon.strip() for weapon in freshfruit]
Out[9]: ['banana', 'loganberry', 'passion fruit']
In [10]: # create a list of 2-tuples like (number, square)
         [(x, x**2) for x in range(6)]
Out[10]: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
In [11]: # the tuple must be parenthesized, otherwise an error is raised
         [x, x**2 for x in range(6)]
          Input In [11]
            [x, x**2 for x in range(6)]
             ^
         SyntaxError: did you forget parentheses around the comprehension target?
In [12]: # flatten a list using a listcomp with two 'for'
         vec = [[1,2,3], [4,5,6], [7,8,9]]
         [num for elem in vec for num in elem]
Out[12]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
List comprehensions juga dapat berisi ekspresi yang kompleks dan fungsi _nested_:

```python
In [13]: from math import pi
         [str(round(pi, i)) for i in range(1, 6)]
Out[13]: ['3.1', '3.14', '3.142', '3.1416', '3.14159']
```
#### 5.1.4. Nested List Comprehensions
Expresi pertama pada sebuah list comprehension bisa berupa ekspresi arbitrary (ekspresi yang dipilih/digunakan sesuai dengan keinginan personal user), atau juga bisa berupa list comprehension lain.

Contoh berikut adalah matriks 4x4 yang diimplementasikan sebagai 3 list yang masing-masing memiliki length 4:

```python
In [1]: matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
```
List comprehension berikut mengubah urutan baris dan kolom:

```python
In [2]: [[row[i] for row in matrix] for i in range(4)]
Out[2]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Seperti yang kita lihat pada _section_ sebelumnya, _nested listcomp_ dievaluasi di dalam konteks for yang mengikuti _nested listcomp_. Jadi contoh tersebut sama dengan:

```python
In [3]: transposed = []
        for i in range(4):
            transposed.append([row[i] for row in matrix])

        transposed
Out[3]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
yang juga sama dengan:

```python
In [4]: transposed = []
        for i in range(4):
        # the following 3 lines implement the nested listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

        transposed
Out[4]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Kita harus menggunakan fungsi built-in untuk statement flow yang kompleks. Kita bisa menggunakan fungsi [zip()](https://docs.python.org/3/library/functions.html#zip) :

```python
In [5]: list(zip(*matrix))
Out[5]: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

### 5.2. Statement `del`
Statement `del` berguna untuk menghapus item dari list pada index yang ditentukan. `del` berbeda dari `pop()` yang me-return nilai. Statement `del` juga bisa digunakan untuk menghapus [slice](https://www.w3schools.com/python/ref_func_slice.asp) dari sebuah list atau juga bisa menghapus seluruh isi list. Contoh:

```python
In [1]: a = [-1, 1, 66.25, 333, 333, 1234.5]
        del a[0]
        a
Out[1]: [1, 66.25, 333, 333, 1234.5]
In [2]: del a[2:4]
        a
Out[2]: [1, 66.25, 1234.5]
In [3]: del a[:]
        a
Out[3]: []
```
[del](https://docs.python.org/3/reference/simple_stmts.html#del) juga bisa digunakan untuk menghapus seluruh variabel:

```python
In [4]: del a
```
### 5.3. Tuple dan Sequence
List dan string memiliki properti yang mirip seperti operasi _indexing_ dan _slicing_. Karena Python merupakan bahasa pemrograman yang masih terus berevolusi, maka selalu ada kemungkinan untuk menambahkan tipe data sequence baru. Python juga memiliki tipe data sequence standar bernama _tuple_.

Tuple berisi kumpulan nilai yang dipisah dengan koma, contoh:

```python
In [1]: t = 12345, 54321, 'hello!'
        t[0]
Out[1]: 12345
In [2]: t
Out[2]: (12345, 54321, 'hello!')
In [3]: # Tuples may be nested:
        u = t, (1, 2, 3, 4, 5)
        u
Out[3]: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
In [4]: # Tuples are immutable:
        t[0] = 88888 
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Input In [4], in <cell line: 2>()
              1 # Tuples are immutable:
        ----> 2 t[0] = 88888

        TypeError: 'tuple' object does not support item assignment

In [5]: # but they can contain mutable objects:
        v = ([1, 2, 3], [3, 2, 1])
        v
Out[5]: ([1, 2, 3], [3, 2, 1])
```
Bisa kita perhatikan jika output tuple pasti ditampilkan di dalam parentheses (tanda kurung), sehingga _nested tuples_ bisa diinterpretasikan dengan benar oleh Python.

Walaupun tuple mirip dengan list, seringkali tuple digunakan pada situasi berbeda dan juga untuk tujuan yang berbeda pula. Tuple bersifat [immutable](https://docs.python.org/3/glossary.html#term-immutable) dan memiliki elemen yang heterogen. Semantara List bersifat [mutable](https://docs.python.org/3/glossary.html#term-mutable) dan memiliki elemen yang homogen.

Tuple empty (kosong) dibentuk oleh sepasang parentheses yang kosong. Tuple dengan satu item dibentuk oleh sebuah value yang diikuti dengan koma. Contoh:

```python
In [6]: empty = ()
        singleton = 'hello', # <-- note trailing comma
        len(empty)
Out[6]: 0
In [7]: len(singleton)
Out[7]: 1
In [8]: singleton
Out[8]: ('hello',)
```
Kita juga bisa melakukan operasi yang merupakan kebalikan dari _tuple packing_. Contoh:

```python
In [9]: x, y, z = t
```
Kode di atas bisa kita sebut dengan _sequence unpacking_. _Sequence unpacking_ dapat mengambil objek dari sebuah _collection_ dan meletakkannya di variabel untuk digunakan pada suatu saat nanti.

### 5.4. Sets
Set adalah sebuah koleksi tidak urut yang tidak memiliki elemen yang diduplikat. Dengan kata lain, set adalah sebuah tipe data kolektif yang bisa digunakan untuk menyimpan nilai dalam satu variabel dengan satu ketentuan yaitu nilai yang disimpan harus berbeda dari yang lain (unik).

Kurung kurawal atau fungsi `set()` bisa digunakan untuk membuat berbagai set. Untuk membuat empty set, kita harus menggunakan `set()`, bukan `{}`. 

Berikut contoh demonstrasi penggunaan set:

```python
In [1]: basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
        print(basket) 
        {'pear', 'orange', 'apple', 'banana'}
In [2]: 'orange' in basket
Out[2]: True
In [3]: 'crabgrass' in basket
Out[3]: False
In [4]: a = set('abracadabra')
        b = set('alacazam')
        a
Out[4]: {'a', 'b', 'c', 'd', 'r'}
In [5]: a - b
Out[5]: {'b', 'd', 'r'}
In [6]: a | b
Out[6]: {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}
In [7]: a & b
Out[7]: {'a', 'c'}
In [8]: a ^ b
Out[8]: {'b', 'd', 'l', 'm', 'r', 'z'}
```
mirip seperti list comprehension, set comprehension juga disupport:

```python
In [9]: a = {x for x in 'abracadabra' if x not in 'abc'}
        a
Out[9]: {'d', 'r'}
```
### 5.5. Dictionaries
Dictionary adalah tipe data pada python yang berfungsi untuk menyimpan kumpulan nilai (value) dengan _key-value_. Dictionary pada bahasa pemrograman lain biasanya berupa array asosiatif. Tidak seperti sequence yang diindex dengan range angka, dictionary diindex dengan _key_ bersifat _immutable_ bertipe string atau angka. Tuple bisa digunakan sebagai key jika tuple tersebut hanya berisi string, angka, dan tuple. Jika tuple tersebut berisi berisi objek _mutable_ baik secara langsung maupun tidak langsung, tuple tersebut tidak bisa digunakan sebagai key dictionary. Kita tidak bisa menggunakan list sebagai key karena list bisa dimodifikasi langsung menggunakan _index assignments_, _slice assignments_, ataupun dengan method seperti `append()` dan `extend()`.

Operasi utama pada dictionary adalah memasukkan value dengan key lalu meng-ekstrak value berdasarkan key. Pada dictionary, penggunaan `list(d)` akan me-return sebuah list berisi seluruh key yang digunakan di dalam dictionary. Untuk memeriksa apakah sebuah key ada di dalam dictionary, kita bisa gunakan keyword [in](https://docs.python.org/3/reference/expressions.html#in).

Berikut contoh penggunaan dictionary:

```python
In [1]: tel = {'jack': 4098, 'sape': 4139}
        tel['guido'] = 4127
        tel
Out[1]: {'jack': 4098, 'sape': 4139, 'guido': 4127}
In [2]: tel['jack']
Out[2]: 4098
In [3]: del tel['sape']
        tel['irv'] = 4127
        tel
Out[3]: {'jack': 4098, 'guido': 4127, 'irv': 4127}
In [4]: list(tel)
Out[4]: ['jack', 'guido', 'irv']
In [5]: sorted(tel)
Out[5]: ['guido', 'irv', 'jack']
In [6]: 'guido' in tel
Out[6]: True
In [7]: 'jack' not in tel
Out[7]: False
```
Konstruktor [dict()](https://docs.python.org/3/library/stdtypes.html#dict) menciptakan dictionaries langsung dari sequence key-value pairs:

```python
In [8]: dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
Out[8]: {'sape': 4139, 'guido': 4127, 'jack': 4098}
```
dict comprehension dapat digunakan untuk menciptakan dictionary dari key arbitrary dan expresi value:

```python
In [9]: {x: x**2 for x in (2, 4, 6)}
Out[9]: {2: 4, 4: 16, 6: 36}
```
Jika key berbentuk string sederhana, maka kita akan lebih mudah dalam menetapkan _pairs_ menggunakan argumen keyword:

```python
In [10]: dict(sape=4139, guido=4127, jack=4098)
Out[10]: {'sape': 4139, 'guido': 4127, 'jack': 4098}
```
### 5.6. Teknik Looping
Ketika melakukan looping melewati dictionary, key dan _corresponding value_ dapat didapatkan pada waktu yang sama menggunakan method `item()`:

```python
In [1]: knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        for k, v in knights.items():
            print(k, v)
        gallahad the pure
        robin the brave
```
Ketika looping melewati sequence, index dan _corresponding value_ bisa didapatkan pada waktu bersamaan menggunakan fungsi [enumerate()](https://docs.python.org/3/library/functions.html#enumerate).

```python
In [2]: for i, v in enumerate(['tic', 'tac', 'toe']):
            print(i, v)
        0 tic
        1 tac
        2 toe
```
Untuk melakukan loop pada dua atau lebih sequence pada waktu yang sama, _entries_ dapat dipasangkan dengan fungsi [zip()](https://docs.python.org/3/library/functions.html#zip).

```python
In [3]: questions = ['name', 'quest', 'favorite color']
        answers = ['lancelot', 'the holy grail', 'blue']
        for q, a in zip(questions, answers):
            print('What is your {0}?  It is {1}.'.format(q, a))
        What is your name?  It is lancelot.
        What is your quest?  It is the holy grail.
        What is your favorite color?  It is blue.
```
Untuk melakukan loop pada sequence secara terbalik, pertama kita harus menetapkan sequence ke arah maju kemudian panggil fungsi [reversed()](https://docs.python.org/3/library/functions.html#reversed).

```python
In [4]: for i in reversed(range(1, 10, 2)):
            print(i)
        9
        7
        5
        3
        1
```
Untuk melakukan loop pada sequence secara urut, gunakan fungsi [sorted()](https://docs.python.org/3/library/functions.html#sorted) yang me-return sebuah list baru yang elemennya urut tanpa mengubah apapun pada list lama.

```python
In [5]: basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        for i in sorted(basket):
            print(i)
        apple
        apple
        banana
        orange
        orange
        pear
```
Menggunakan [set](https://docs.python.org/3/library/stdtypes.html#set) pada sebuah sequence dapat menghapus elemen duplikat. Kombinasi sorted() dan set() pada sebuah sequence merupakan cara idiomatis untuk melakukan loop pada elemen unik milik sequence secara urut.

```python
In [6]: basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        for f in sorted(set(basket)):
            print(f)
        apple
        banana
        orange
        pear
```
Kadangkala kita ingin mengganti list pada saat kita melakukan loop. Walau begitu, sebenarnya lebih mudah dan lebih aman jika kita membuat list baru.

```python
In [7]: import math
        raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
        filtered_data = []
        for value in raw_data:
            if not math.isnan(value):
                filtered_data.append(value)

        filtered_data
Out[7]: [56.2, 51.7, 55.3, 52.5, 47.8]
```
### 5.7. Lebih Banyak tentang Kondisi
Kondisi yang digunakan di statement `while` dan `if` dapat berisi segala operator, tidak hanya perbandingan.

Operator perbandingan `in` dan `not in` adalah _membership tests_ yang menentukan apakah nilai ada di dalam kontainer atau tidak. Operator `is` dan `is not` membandingkan apakah dua objek merupakan objek yang sama.

Perbandingan dapat diikat (digabung). Misalnya, `a < b == c`. Perbandingan juga dapat dikombinasikan menggunakan operator Boolean yaitu `and` dan `or`, dan hasil dari perbandingan tersebut bisa dinegasikan dengan `not`.

Kita bisa menempatkan hasil dari perbandingan atau expresi Boolean lain ke dalam sebuah variabel. Contoh:

```python
In [1]: string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
        non_null = string1 or string2 or string3
        non_null
Out[1]: 'Trondheim'
```
### 5.8. Membandingkan Sequence dan Tipe Lain
Objek sequence biasanya dibandingkan dengan objek lain yang memiliki tipe sequence sama. Pembanding menggunakan urutan _lexicographical_: pertama, dua item pertama dibandingkan. Jika dua item tersebut berbeda maka hal ini dapat menentukan hasil dari perbandingan. Jika dua item setara, maka dua item selanjutnya dibandingkan. Begitu terus hingga sequence selesai. 

Urutan _lexicographical_ untuk string menggunakan angka unicode point untuk mengurutkan karakter individual. Contoh perbandingan antara sequence yang memiliki tipe sama:

```python
In [1]: (1, 2, 3)              < (1, 2, 4)
        [1, 2, 3]              < [1, 2, 4]
        'ABC' < 'C' < 'Pascal' < 'Python'
        (1, 2, 3, 4)           < (1, 2, 4)
        (1, 2)                 < (1, 2, -1)
        (1, 2, 3)             == (1.0, 2.0, 3.0)
        (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
Out[1]: True
```
Bisa kita perhatikan bahwa membandingkan objek dengan tipe berbeda dengan `< or >` diperbolehkan, asalkan objek memiliki metode perbandingan yang sesuai. Contohnya, tipe numerik campuran dapat dibandingkan menurut nilai numeriknya, misalnya `0` sama dengan `0.0`.