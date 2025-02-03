tensao = 4.5112

tensao_no_indutor = 5 - tensao
corrente = tensao / 200
resistencia_indutor = tensao_no_indutor/corrente

print(resistencia_indutor)