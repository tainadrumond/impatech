import matplotlib.pyplot as plt
import pandas as pd

# Importar os dados do arquivo CSV
data = pd.read_csv('p2c.csv')

# Configurar os dados para o gráfico
time = data['Time(s)']
ch1 = data['CH1V']
ch2 = data['CH2V']

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(time, ch1, label='CH1V', color='blue')
plt.plot(time, ch2, label='CH2V', color='orange')

# Configurar rótulos e título
plt.xlabel('Tempo (s)')
plt.ylabel('Voltagem (V)')
plt.title('Gráfico de Voltagem vs. Tempo')
plt.legend()
plt.grid(True)

# Mostrar o gráfico
plt.show()
