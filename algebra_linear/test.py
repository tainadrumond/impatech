from matrix import Matrix, Vector
from gaussian_elimination import gaussian_elimination

############ Vector
print("tests for Vector class")
v1 = Vector([1, 0, 0])
v2 = Vector(size=3)
v3 = Vector([1, 2, 3.4])
v4 = v3.copy()
v4.change_entry(0, 1)
print(v1, v2, v3*2, v4)
v5 = Vector([1, 2, 3, 4, 5, 6])
print(v5.length)
print(v5.at(4))

############## Matrix
print("\ntests for Matrix class") 
m1 = Matrix([v1, v2, v3])
print(m1)

print()

m2 = m1.copy()
m2.change_entry(1000, 1, 1)
print(m2)

print()

m3 = m1.copy()
print(m3.at(2, 2))
print(m3*2)

############## Gaussian elimination
print("\n tests for gaussian elimination")
gaussian_elimination_1 = gaussian_elimination(m3)
print(f'A:\n{m3}')
print(f'P:\n{gaussian_elimination_1['P']}')
print(f'L:\n{gaussian_elimination_1['L']}')
print(f'U:\n{gaussian_elimination_1['U']}')

a1 = Vector([0, 2])
a2 = Vector([0, 1])
a3 = Vector([8, 6])
A = Matrix([a1, a2, a3])
gaussian_elimination_2 = gaussian_elimination(A)
print(f'A:\n{A}')
print(f'P:\n{gaussian_elimination_2['P']}')
print(f'L:\n{gaussian_elimination_2['L']}')
print(f'U:\n{gaussian_elimination_2['U']}')
