from canonical_form import to_canonical_form
import numpy as np

def test_to_canonical_form1():
    # Exemplo simples para teste
    A = np.array([
        [1, 2, 1, 0],
        [2, 1, 0, 1]
    ], dtype=np.float64)
    b = np.array([4, 3], dtype=np.float64)
    c = np.array([3, 2, 0, 0], dtype=np.float64)
    z = np.array([0], dtype=np.float64)  # termo constante do objetivo

    # Executa a transformação
    B, N, A_canon, b_canon, c_canon, z_canon = to_canonical_form(A, b, c, z)

    # Valores esperados
    expected_B = [0, 1]  # colunas básicas (as duas primeiras)
    expected_N = [2, 3]  # colunas não básicas
    expected_A_canon = np.array([
        [1, 0, -1/3, 2/3],
        [0, 1, 2/3, -1/3]
    ], dtype=np.float64)
    expected_b_canon = np.array([1.6, 1.4], dtype=np.float64)
    expected_c_canon = np.array([0, 0, -1.0, -0.5], dtype=np.float64)
    expected_z_canon = np.array([10.0], dtype=np.float64)
    
    print(A_canon)

    # Testes
    assert B == expected_B, f"B does not match expected. Got {B}, expected {expected_B}"
    assert N == expected_N, f"N does not match expected. Got {N}, expected {expected_N}"
    assert np.allclose(A_canon, expected_A_canon), f"A_canon does not match expected.\nGot\n{A_canon}\nExpected\n{expected_A_canon}"
    assert np.allclose(b_canon, expected_b_canon), f"b_canon does not match expected.\nGot\n{b_canon}\nExpected\n{expected_b_canon}"
    assert np.allclose(c_canon, expected_c_canon), f"c_canon does not match expected.\nGot\n{c_canon}\nExpected\n{expected_c_canon}"
    assert np.allclose(z_canon, expected_z_canon), f"z_canon does not match expected.\nGot\n{z_canon}\nExpected\n{expected_z_canon}"

    print("All tests passed!")

# Executa o teste
test_to_canonical_form1()
