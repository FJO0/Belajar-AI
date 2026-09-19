import numpy as jo

# soal nomor 1
i = jo.array([[4, 5], [3, 6]])
j = jo.array([[2, 2], [3, 2]])

# perkalian
r =jo.dot(i, j)
print( r ) 

# pembagian
print( i / j )

# penjumlahan
print( i + j )

# pengurangan
print( i - j )

# soal nomor 2

def array_random():
    return jo.random.randint(1, 21, (3, 3))

t = array_random()
print("sebelum :", t)

def aturan_array(data):
    data[data > 10] = 20
    data[data < 10] = 0
    return data

c = aturan_array(t)
print("sesudah :", c)