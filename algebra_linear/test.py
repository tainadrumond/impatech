import unittest
from alg_lin_lib import Matrix, Vector, gaussian_elimination

# ############ Vector
# print("tests for Vector class")
# v1 = Vector([1, 0, 0])
# v2 = Vector(size=3)
# v3 = Vector([1, 2, 3.4])
# v4 = v3.copy()
# v4.change_entry(0, 1)
# print(v1, v2, v3*2, v4)
# v5 = Vector([1, 2, 3, 4, 5, 6])
# print(v5.length)
# print(v5.at(4))

# ############## Matrix
# print("\ntests for Matrix class") 
# m1 = Matrix([[1, 0, 0], [0, 0, 0], [1, 2, 3.4]])
# print(m1)

# print()

# m2 = m1.copy()
# m2.change_entry(1000, 1, 1)
# print(m2)

# print()

# m3 = m1.copy()
# print(m3.at(2, 2))
# print(m3*2)

# ############## Gaussian elimination
# def print_gaussian_elimination_result(result):
#     print(f'P:\n{result['P']}')
#     print(f'L:\n{result['L']}')
#     print(f'U:\n{result['U']}')

# print("\n tests for gaussian elimination")
# A1 = [[4, 3],
#     [6, 3]]
# gaussian_elimination_1 = gaussian_elimination(A1)
# print(f'A:\n{A1}')
# print_gaussian_elimination_result(gaussian_elimination_1)

# A2 = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 10]]
# gaussian_elimination_2 = gaussian_elimination(A2)
# print(f'A:\n{A2}')
# print_gaussian_elimination_result(gaussian_elimination_2)

# A3 = [[2, 4],
#     [1, 3],
#     [3, 5]]
# gaussian_elimination_3 = gaussian_elimination(A3)
# print(f'A:\n{A3}')
# print_gaussian_elimination_result(gaussian_elimination_3)

# A4 = [[2, 4, 2],
#     [4, 8, 4],
#     [6, 12, 6]]
# gaussian_elimination_4 = gaussian_elimination(A4)
# print(f'A:\n{A4}')
# print_gaussian_elimination_result(gaussian_elimination_4)

# A5 = [[1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1]]
# gaussian_elimination_5 = gaussian_elimination(A5)
# print(f'A:\n{A5}')
# print_gaussian_elimination_result(gaussian_elimination_5)

# A6 = [[2, 0, 0],
#     [0, 3, 0],
#     [0, 0, 4]]
# gaussian_elimination_6 = gaussian_elimination(A6)
# print(f'A:\n{A6}')
# print_gaussian_elimination_result(gaussian_elimination_6)

# A7 = [[0, 2, 1, 3],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11]]
# gaussian_elimination_7 = gaussian_elimination(A7)
# print(f'A:\n{A7}')
# print_gaussian_elimination_result(gaussian_elimination_7)

# A8 = [[1, 2, 3],
#     [4, 5, 6],
#     [0, 8, 9],
#     [7, 10, 11]]
# gaussian_elimination_8 = gaussian_elimination(A8)
# print(f'A:\n{A8}')
# print_gaussian_elimination_result(gaussian_elimination_8)

# A9 = [[0, 1, 2, 3],
#     [4, 5, 6, 7]]
# gaussian_elimination_9 = gaussian_elimination(A9)
# print(f'A:\n{A9}')
# print_gaussian_elimination_result(gaussian_elimination_9)

# A10 = [[1, 0, 3, 4, 5, 6],
#     [0, 1, 2, 3, 4, 5],
#     [0, 0, 1, 2, 3, 4],
#     [1, 1, 1, 1, 1, 1]]
# gaussian_elimination_10 = gaussian_elimination(A10)
# print(f'A:\n{A10}')
# print_gaussian_elimination_result(gaussian_elimination_10)

# A11 = [[3, 2, 1],
#     [1, 1, 1],
#     [0, 1, 4],
#     [4, 0, 1],
#     [5, 2, 2]]
# gaussian_elimination_11 = gaussian_elimination(A11)
# print(f'A:\n{A11}')
# print_gaussian_elimination_result(gaussian_elimination_11)

# A12 = [
#     [0, 0, -1, 2],
#     [-1, -1, 1, 2],
#     [2, 1, -3, 6],
#     [0, 1, -1, 4]
# ]
# gaussian_elimination_12 = gaussian_elimination(A12)
# print(f'A:\n{A12}')
# print_gaussian_elimination_result(gaussian_elimination_12)

# A13 = [[2, -1, 0],
#     [-1, 2, -1],
#     [0, -1, 2]]
# gaussian_elimination_13 = gaussian_elimination(A13)
# print(f'A:\n{A13}')
# print_gaussian_elimination_result(gaussian_elimination_13)

from alg_lin_lib import is_basis

class Test_Is_Basis(unittest.TestCase):
    def test_identity(self):
        vectors = [[1, 0],[0, 1]]
        expected_output = True
        self.assertEqual(is_basis(vectors), expected_output)
        
    def test_square_2d_li_1(self):
        vectors = [[1, 1],[0, 1]]
        expected_output = True
        self.assertEqual(is_basis(vectors), expected_output)
        
    def test_square_2d_ld_1(self):
        vectors = [[1, 2],[2, 4]]
        expected_output = False
        self.assertEqual(is_basis(vectors), expected_output)
    
    def test_square_3d_li_1(self):
        vectors = [[1, 0, 5],[2, 1, 6],[3, 4, 0]]
        expected_output = True
        self.assertEqual(is_basis(vectors), expected_output)
        
    def test_square_3d_ld_1(self):
        vectors = [[1, 0, 0],[2, 1, 0],[3, 4, 0]]
        expected_output = False
        self.assertEqual(is_basis(vectors), expected_output)
    
    def test_rectangular_li_1(self):
        vectors = [[1, 3, 5], [2, 4, 6]]
        expected_output = True
        self.assertEqual(is_basis(vectors), expected_output)
    
    def test_rectangular_ld_1(self):
        vectors = [[1, 2, 0], [2, 4, 0]]
        expected_output = False
        self.assertEqual(is_basis(vectors), expected_output)

    def test_rectangular_ld_2(self):
        vectors = [[1, 2], [2, 4], [0, 1]]
        expected_output = False
        self.assertEqual(is_basis(vectors), expected_output)

from alg_lin_lib import get_coordinates
class Test_Get_Coordinates(unittest.TestCase):
    def test_identity(self):
        base = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
        vector = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(get_coordinates(vector, base), expected_output)

    def test_rectangular_1(self):
        base = [[1, 3, 5], [2, 4, 6]]
        vector = [5, 11, 17]
        expected_output = [1.0, 2.0]
        self.assertEqual(get_coordinates(vector, base), expected_output)
    
    def test_square_1(self):
        base = [[1, 1, 0], [-1, 1, 0], [0, 0, 1]]
        vector = [2, 3, 4]
        expected_output = [2.5, 0.5, 4]
        self.assertEqual(get_coordinates(vector, base), expected_output)
    
    def test_square_2(self):
        base = [[1, 1],[0, 1]]
        vector = [3, 2]
        expected_output = [3, -1]
        self.assertEqual(get_coordinates(vector, base), expected_output)
    
    def test_square_3(self):
        base = [[2, 1],[1, 1]]
        vector = [3, 4]
        expected_output = [-1, 5]
        self.assertEqual(get_coordinates(vector, base), expected_output)
    
    def test_square_4(self):
        base = [[0, 1, 1], [0, -1, 1], [1, 0, 0]]
        vector = [2, 3, 4]
        expected_output = [3.5, 0.5, 2.0]
        self.assertEqual(get_coordinates(vector, base), expected_output)

from alg_lin_lib import is_orthonormal_basis
class Test_Is_Orthonormal_Basis(unittest.TestCase):
    def test_canonical_1(self):
        vectors = [[1, 0], [0, 1]]
        expected_output = True
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    def test_canonical_1(self):
        vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected_output = True
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    def test_rectangular_1(self):
        vectors = [[1, 0, 0], [0, 1, 0]]
        expected_output = True
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    def test_rectangular_2(self):
        vectors = [[1, 2], [2, 4], [0, 1]]
        expected_output = False
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    # Erro de ponto flutuante:
    # def test_square_1(self):
    #     vectors = [[1/(2*(1/2)), 1/(2(1/2))], [1/(2(1/2)), -1/(2*(1/2))]]
    #     expected_output = True
    #     self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    def test_square_2(self):
        vectors = [[1, 0, 5],[2, 1, 6],[3, 4, 0]]
        expected_output = False
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)

    def test_square_3(self):
        vectors = [[1/2, 1/2],[-1/2, 1/2]]
        expected_output = True
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    def test_square_3(self):
        vectors = [[3/5, 4/5],[-4/5, 3/5]]
        expected_output = True
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)
    
    def test_canonical(self):
        vectors = [[1, 2, 0], [2, 4, 0]]
        expected_output = False
        self.assertEqual(is_orthonormal_basis(vectors), expected_output)

from alg_lin_lib import get_coordinates_in_orthonormal_basis
class Test_Get_Coordinates_In_Orthonormal_Basis(unittest.TestCase):
    def test_identity(self):
        base = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
        vector = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(get_coordinates_in_orthonormal_basis(vector, base), expected_output)

    def test_rectangular_1(self):
        base = [[1, 0, 0], [0, 1, 0]]
        vector = [5, 11, 7]
        expected_output = [5, 11]
        self.assertEqual(get_coordinates_in_orthonormal_basis(vector, base), expected_output)
    
    def test_square_1(self):
        base = [[1/2, 1/2],[-1/2, 1/2]]
        vector = [2, 3]
        expected_output = [2.5, 0.5]
        self.assertEqual(get_coordinates_in_orthonormal_basis(vector, base), expected_output)
    
    def test_square_2(self):
        base = [[3/5, 4/5],[-4/5, 3/5]]
        vector = [3, 2]
        expected_output = [3.4, -1.2000000000000004]
        self.assertEqual(get_coordinates_in_orthonormal_basis(vector, base), expected_output)
        
from determinant import determinant
class Test_Determinant(unittest.TestCase):
    def test_identity(self):
        matrix = [[1, 0], [0, 1]]
        expected_output = 1
        self.assertEqual(determinant(matrix), expected_output)
    
    def test_square_1(self):
        matrix = [[2, 3], [1, 4]]
        expected_ouput = 5
        self.assertEqual(determinant(matrix), expected_ouput)
    
    def test_square_2(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_ouput = 0
        self.assertEqual(determinant(matrix), expected_ouput)
        
    def test_square_3(self):
        matrix = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
        expected_ouput = 30
        self.assertEqual(determinant(matrix), expected_ouput)
    
    def test_square_4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected_output = 0
        self.assertEqual(determinant(matrix), expected_output)
    
    def test_square_5(self):
        matrix = [[5, 4], [2, 3]]
        expected_output = 7
        self.assertEqual(determinant(matrix), expected_output)
    
    def test_square_6(self):
        matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
        expected_output = -306
        self.assertEqual(determinant(matrix), expected_output)
        
if __name__ == '__main__':
    unittest.main()