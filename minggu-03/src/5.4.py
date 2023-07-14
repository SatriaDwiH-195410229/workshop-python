basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # menunjukkan jika duplikat sudah dihapus
print('orange' in basket) # fast membership testing

print('crabgrass' in basket)


# Demonstrasi operasi set pada huruf untuk dari dua kata

a = set('abracadabra')
b = set('alacazam')
print(a) # huruf unik di a
print(a - b)# huruf di a tapi tidak di b
print(a | b)# huruf di a atau b atau di keduanya
print(a & b)# huruf di a dan b
print(a ^ b)# huruf di a atau b tapi tidak di keduanya

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)