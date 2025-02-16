import csv

with open('dados.csv', mode='a', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([200,700])