import numpy as np

X = np.array([3.85, 3.88, 1.46, 3.74, 3.69, 1.19, 3.06, 1.13, 1.11, 2.24, 4.00, 1.99, 2.40, 2.04, 1.31])
Y = np.array([4.95, 6.63, 4.65, 6.03, 5.26, 3.71, 6.06, 5.19, 3.37, 3.71])

# Item A: Estimação para a mediana
# Obtive as medianas dos próprios arrays de entrada:s
median_x = np.median(X)
median_y = np.median(Y)

print(f"Mediana estimada para X: {median_x}")
print(f"Mediana estimada para Y: {median_y}")
print()

# Item B: Estimação para incerteza da mediana usando bootstrap
def median_bootstrap(arr, B):
    sample_size = len(arr)
    medians = np.array([])
    
    # Gera B amostras com reposição e calcula suas medianas
    for _ in range(B):
        sample = np.random.choice(arr, sample_size, replace=True) # sorteio com reposição
        medians = np.append(medians, np.median(sample)) # adiciona a mediana do sample atual ao array de resultados
    
    mean = np.mean(medians)
    se = np.var(medians)**0.5 # erro padrão das medianas das amostras geradas
    
    return medians, mean, se

B = 5000
medians_x, mean_x, se_x = median_bootstrap(X, B)
medians_y, mean_y, se_y = median_bootstrap(Y, B)

print(f"Erro padrão da mediana de X calculado com bootstrap: {se_x}")
print(f"Erro padrão da mediana de Y calculado com bootstrap: {se_y}")
print()

# Item C: Construção do intervalo de confiança
def confidence_set(arr, alpha):
    lower_bound = np.quantile(arr, alpha/2) # limite inferior do intervalo (quantil alpha/2)
    upper_bound = np.quantile(arr, 1-(alpha/2)) # limite superior do intervalo (quantil 1-alpha/2)
    return (lower_bound, upper_bound)

alpha = 0.1 # alpha para a construção de um intervalo de confiança de 90%
x_confidence_set = confidence_set(medians_x, alpha)
y_confidence_set = confidence_set(medians_y, alpha)

print(f"Intervalo de confiança para a mediana de X com bootstrap: {x_confidence_set}")
print(f"Intervalo de confiança para a mediana de Y com bootstrap: {y_confidence_set}")
print()

# Item D: 
# Vamos analizar o resultado de uma execução do algoritmo:
# Mediana estimada para X: 2.24
# Mediana estimada para Y: 5.07

# Erro padrão da mediana de X calculado com bootstrap: 0.5898524790453966
# Erro padrão da mediana de Y calculado com bootstrap: 0.5066619062047195

# Intervalo de confiança para a mediana de X com bootstrap: (1.46, 3.69)
# Intervalo de confiança para a mediana de Y com bootstrap: (4.18, 6.03)

# Perceba que os intervalos de confiança são disjuntos. Isso nos dá uma forte evidência
# de que as medianas são diferentes.