'''
# angka dari 1-100 ambil genapnya aja, lalu masing2 dikali 2, lalu semuanya dijumlahkan
nomor = range(1, 101)

from functools import reduce

hasil = reduce(lambda x, y: x + y, list(map(lambda a : a * 2, list(filter(lambda a : a % 2 == 0, nomor)))))
print(hasil)

# angka dari 0-100 ambil bilangan primanya aja
def prima(x):
    a = False
    if x > 1:
        if x == 2:
            a = True
        else:
            for  i in range(2, x):
                if x % i == 0:
                    a = False
                    break
                else:
                    a = True
    else:
        a = False
    return a

primanya = list(filter(prima, range(101)))
print(primanya)
'''
