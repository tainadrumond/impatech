# Calcula o produto externo do vetor l1 pelo vetor l2
def outerProduct(l1: list, l2: list) -> list:
    r = []
    # Para cada iteração, calcula o vetor resultante do produto do primeiro escalar de l1 pelo vetor l2
    for n1 in l1:
        c = []
        r.append(c)
        # Faz o produto de cada elemento de l2 pelo escalar de l1
        for n2 in l2:
            c.append(n1*n2)
    return r

mcc1 = outerProduct([1], [3, 5, 6])
mcc2 = outerProduct([1, 2], [3, 5, 6])
print(mcc1)
print(mcc2)