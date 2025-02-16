import serial
import time
import pyvisa
import numpy as np
import csv

is_first_heat = True 

def get_temp(tensao):
    resistencia = 10000*tensao/(5-tensao)
    temp = 7017.28/(np.log(resistencia/10000)+(7017.28/298.15))
    return temp - 273.15

def get_u(prev_u, volt_lida, volt_esperada, prev_e, kp, ki, t):
    global is_first_heat
    
    e = volt_lida - volt_esperada
    
    u = prev_u + (kp*(e - prev_e)) + (ki*t*e)
    u = 0 if u < 0 else u
    u = 2.5 if u > 2.5 else u
    
    return u

# Configurar comunicação com Arduino
arduino = serial.Serial("COM5", 9600, timeout=1)
time.sleep(2)  # Aguarda a inicialização do Arduino

# Configurar comunicação com a Rigol DP932U via Ultra Sigma
rm = pyvisa.ResourceManager()

fonte = rm.open_resource("USB0::0x1AB1::0xA4A8::DP9C243400240::INSTR")  # Ajuste para seu dispositivo
fonte.write("*IDN?")  # Testa conexão
print(fonte.read())

# Ligango o canal 1
fonte.write(f":APPL CH1,0,0.5")
fonte.write(":OUTP CH1,ON")

# Ligando o canal 2
fonte.write(f":APPL CH2,0,0.5")
fonte.write(":OUTP CH2,ON")

# Variáveis auxiliares
prev_u = 0
prev_e = 0
tempo = 0

# Constantes utilizadas
kp = 40
ki = 0.01


while True:
    if arduino.in_waiting > 0:
        # Lendo os dados da entrada 
        linha = arduino.readline().decode("utf-8").strip()
        
        volt_esperada = float(linha.split()[0]) 
        volt_lida = float(linha.split()[1])
        
        # Obtendo as temperaturas em graus Celsius com base na tensão
        temp_esperada = get_temp(volt_esperada)
        temp_lida = get_temp(volt_lida)
        
        # Escrita dos dados no arquivo
        with open('dados.csv', mode='a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([temp_esperada,temp_lida,prev_u])
        
        # Cálculo da próxima tensão a ser aplicada com base no PI
        curr_u = get_u(prev_u, volt_lida, volt_esperada, prev_e, kp, ki, tempo)

        # Aplicando as tensões na fonte
        fonte.write(f":APPL CH1,{curr_u},0.5")
        print(f"Setando canal 1 para {curr_u}V")
        
        fonte.write(f":APPL CH2,{curr_u*1.44},0.5")
        print(f"Setando canal 2 para {curr_u*(2**(1/2))}V")
        
        # Salvando as variáveis para a próxima iteração
        prev_u = curr_u
        prev_e = volt_lida - volt_esperada 
        
    time.sleep(1)
    tempo += 1
