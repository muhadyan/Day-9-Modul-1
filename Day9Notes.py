'''
# LAMBDA FUNCTION
x = lambda a : a
print(x(2))
# mirip dengan
def y(a):
    return a
print(y(2))


x = lambda a,b,c : a+b+c
print(x(2,3,4))
# mirip dengan
def y(a,b,c):
    return a+b+c
print(y(2,3,4))

# lambda function di dalam def function
def myFunction(x):
    return lambda a : a ** x

pangkat2 = myFunction(2)
pangkat3 = myFunction(3)

print(pangkat2(12))
print(pangkat3(4))

# bikin if else pake lambda function
x = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'    # harus satu baris karna lambda itu cuma satu expression

print(x(4))



# MAP
def y(a):
    return len(a)
b = ['Andi', 'Budi', 'Caca']

x = map(y, b)
print(list(x))      # keluar len dari setiap elemen di list

x = map(y, 'Purwadhika')
print(list(x))      # keluarnya len dari setiap huruf di string(karna objectnya string)


# contoh map
a = ['Cokelat', 'Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']
def combi(a, b):
    return a+' '+b
x = map(combi, a, b)
print(list(x))


# contoh map
x = [2, 3, 6, 8, 10]
def pangkat(x):
    return x ** 2
a = map(pangkat, x)
print(list(a))
# atau
x = [2, 3, 6, 8, 10]
pangkat = lambda x : x ** 2
a = map(pangkat, x)
print(list(a))
# atau
z = map(lambda a : a ** 2, x)       # lambda bisa langsung dijalankan di dalam map juga
print(list(z))

# menggunakan function bawaan python
z = list(map(pow, [2, 3], [2, 3]))      # 'elemen 0 di list pertama' pangkat 'elemen 0 di list kedua', dst
print(z)



# FILTER
x = range(11)
def kurangLima(x):
    if x < 5:
        return False
    else:
        return True

y = filter(kurangLima, x)       # si def 'if else'nya harus boolean
print(list(y))
# bisa juga
z = filter(lambda a: True if a >= 5 else False, x)
print(list(z))
# atau
z = filter(lambda a: a >= 5, x)
print(list(z))



# REDUCE FUNCTION
from functools import reduce    # jika ingin import tapi ga semua functionnya 
angka = [1, 2, 3, 4]

z = reduce(lambda x, y: x * y, angka)   # x adalah elemen sebelumnya dan y adalah elemen selanjutnya di dalam sebuah list
print(z)

kata = ['Ini', 'Ibu', 'Budi']
gabung = reduce(lambda x, y: x+' '+y, kata)
print(gabung)
# atau
print(' '.join(kata))


# filter in map
angka = [1, 2, 3, 4]

z = list(map(lambda x : x + x, filter(lambda x : x > 2, angka)))        # filter di dalem map
print(z)

z = list(filter(lambda x : x > 2, map(lambda x : x + x, angka)))        # map di dalem filter
print(z)
'''