from matrix import Matrix, Vector

m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

print(m1)
print(m1.shape)

print(m1.T())
print(m1.T().shape)

m2 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])

m3 = Matrix([[0.0, 1.0],
             [2.0, 3.0],
             [4.0, 5.0],
             [6.0, 7.0]])

print(m2 * m3)

v1 = Vector([[1], [2], [3]])
m4 = Matrix([[0.0, 1.0, 2.0],
             [0.0, 2.0, 4.0]])

print(m4 * v1)

v2 = Vector([[2], [4], [8]])
print(v1 + v2)

print(v1.dot(v2))

print(m1 + Matrix([[1, 1], [1, 1], [1, 1]]))

print(m1 * 2)

print(m1 / 2)