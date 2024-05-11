import numpy as np

def quadratic_adjustment(x, y):
	m1 = []
	m2 = []

	for i in x:
		m1.append([1, i, i**2])
	for i2 in y:
		m2.append([i2])

	A = np.array(m1)

	C=A.T@np.array(m2)

	AI=(np.linalg.inv(A.T@A))

	a = str(round(((AI@C)[2][0]),5))
	b = str(round(((AI@C)[1][0]),5))
	c = str(round(((AI@C)[0][0]),5))
	return [float(a), float(b), float(c)]