import matplotlib.pyplot as plt

# Dados
resistencia = [300, 600, 900, 1200, 1500, 1510]
tensao = [0.9922, 1.9892, 2.9863, 3.9785, 4.9658, 5.0000]

# Incertezas nas medições
resistencia_error = [34, 34, 30, 26, 21, 15]

# Visualização das incertezas
plt.errorbar(resistencia, tensao, xerr=resistencia_error, fmt='o', 
             capsize=5, linestyle='None', color='blue', label='Incerteza das resistências')

# Plotando os pontos dos valores medidos 
plt.scatter(resistencia, tensao, color="blue", label="Dados experimentais")
plt.title("Tensão x Resistência")
plt.xlabel("Resistência (Ω)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)

# Gráfico do ajuste
x_app = [0, 1500]
y_app = [0, 4.9658]
plt.plot(x_app, y_app, color = "orange", label="V = 0.00331 x R")

# Exibindo o gráfico
plt.legend()
plt.show()
