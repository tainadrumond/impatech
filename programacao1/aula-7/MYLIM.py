def limReal(f, from_the_right, a, n, verbose = False):
    for i in range(n):
        delta = 1.0/(i+1)
        if not from_the_right:
            delta *= -1.0
        l = f(a + delta)
        if verbose:
            print(f'delta = {delta}, f({a+delta})={l}')
    return l