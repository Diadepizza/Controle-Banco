import serial
from db import conectar
import time

arduino = serial.Serial('COM4', 9600)
conexao = conectar()
cursor = conexao.cursor()

ultimo_tempo = time.time()

while True:
    dado = arduino.readline().decode().strip()

    if dado == "REGISTRADO":
        agora = time.time()
        intervalo = agora - ultimo_tempo
        ultimo_tempo = agora

        print("Intervalo:", intervalo)

        cursor.execute(f"INSERT INTO producao(intervalo) VALUES ({intervalo})")
        conexao.commit()