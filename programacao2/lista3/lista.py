from lib import Vector3D

# EXERCÍCIO 1 
class NumericalVector3D(Vector3D):
    epsilon = 2.220446049250313e-16 # Positive epsilon
    neg_epsilon = -2.220446049250313e-16 # Negative epsilon
    
    def __eq__(self, other_vector):
        # Para cada coordenada, checa se o valor absoluto da diferença entre o vetor 
        # atual e o outro vetor é maior que epsilon para determinar se os número podem, 
        # de fato, serem considerados diferentes.
        for i in range(self._dim):
            if abs(self.coord[i] - other_vector.coord[i]) > self.epsilon:
                return False
        return True
    
    def __lt__(self, other_vector):
        # Checa se o outro vetor é maior que o atual a uma distância superior a epsilon.
        return other_vector.__abs__() - self.__abs__() > self.epsilon
    
    def __le__(self, other_vector):
        # Checa se a diferença está ao redor do valor de epsilon ou se o outro vetor é 
        # maior que o atual a uma distância superior a epsilon.
        return other_vector.__abs__() - self.__abs__() > self.neg_epsilon
    
    def __gt__(self, other_vector):
        # Checa se o vetor atual é maior que o outro vetor a uma distância superior a epsilon.
        return self.__abs__() - other_vector.__abs__() > self.epsilon
    
    def __ge__(self, other_vector):
        # Checa se a diferença está ao redor do valor de epsilon ou se o vetor atual é 
        # maior que o outro vetor a uma distância superior a epsilon.
        return self.__abs__() - other_vector.__abs__() > self.neg_epsilon
    
    
# EXERCÍCIO 2
# - Para o sinal, precisamos de 1 bit

# - Para os números de d_0 até d_(p-1), temos p algarismos.
#   Para cada um desses algarismos, como eles estão na base beta, precisamos de log2(beta) bits.
#   Logo, para todos os algarismos, precisamos de p*log2(beta)

# - Para o expoente, precisamos representar todos os números no intervalo [e_min, e_max].
#   Como são inteiros, temos um total de e_max-e_min+1 números no intervalo.
#   Considerando que e_min e e_max também estão na base beta, precisamos de log2(e_max-e_min+1) bits

#   No total, temos 1 + p*log2(beta) + log2(e_max-e_min+1) bits necessários.


# EXERCÍCIO 3
def calculate_machine_epsilon_around_1():
    # Calcula o valor de epsilon diminuindo-o, iterativamente, até que alcance um valor 
    # que não cause diferença entre o número somado a ele e o próprio número. 
    epsilon = 1
    while 1 + epsilon != 1:
        epsilon = epsilon/2
    return epsilon * 2 # Retorna ao último epsilon que ainda causava diferença

# EXERCÍCIO 4
def calculate_machine_epsilon_around_e6():
    epsilon = 1.0
    while 1e6 + epsilon != 1e6:
        epsilon = epsilon/2
    return epsilon * 2

# O epsilon de máquina em torno de 1 está na ordem de 10^-16, enquanto em torno de 1000000 
# está na ordem de 10^-10. Isso indica que, ao lidar com números muito grandes, a precisão
# é significativamente reduzida. Em aplicações que lidam com números de ordem de grandeza
# grande, é esperado que a precisão dos dados seja menor, e isso deve ser levado em
# consideração para não gerar muitos erros de imprecisão.


# EXERCÍCIO 5
# Eu criaria uma classe que salva a parte inteira e a parte decimal do número em atributos 
# diferentes. Essa classe implementaria as operações númericas necessárias tratando 
# separadamente a parte inteira e a parte decimal, fazendo as devidas conversões.
# Dessa forma, tanto a parte inteira quanto a parte decimal teriam a precisão 
# necessária, garantindo que os quilômetros e os milímetros sejam preservados. 