# Exercício 2 
# 
# a)
# Renomear a função __ints__ para __init__
# 
# b)
# A saída esperada será:
# []
# [2.0, 1.0]
# 
# c)
# A função add não faz de fato o que ela documenta.
# A linha 20 (new_vector[i] = self.values[i] + self.values[i])
# faz com a função add multiplique por 2 as entradas do vetor na 
# qual ela foi chamada, e não com que adicione o vetor passado
# como parâmetro.
# Caso a função realmente adicionasse os dois vetores, a linha 20 seria:
# new_vector[i] = self.values[i] + other_vector.values[i]
