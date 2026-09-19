import numpy as jo

king = jo.array([[1, 2, 3], [4, 5, 6]])

for i in jo.nditer(king) :
    print(i)