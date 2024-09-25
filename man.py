import pyautogui
import keyboard
import threading
from time import sleep

# Variável para controlar a execução
running = True

# Função para monitorar a tecla de interrupção
def monitor_stop_key():
    global running
    # Fica monitorando até que 'q' seja pressionada
    while running:
        if keyboard.is_pressed('q'):
            running = False
            print("Interrompido pelo usuário.")
            break

# Inicia o monitoramento da tecla em um thread separado
thread = threading.Thread(target=monitor_stop_key)
thread.start()

with open('Goal_Scorers.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # Se running for False, interrompe o loop
        if not running:
            break
        
        date = linha.split(',')[0]
        home_team = linha.split(',')[1]
        away_team = linha.split(',')[2]
        team = linha.split(',')[3]
        scorer = linha.split(',')[4]
        minute = linha.split(',')[5]
        own_goal = linha.split(',')[6]
        penalty = linha.split(',')[7]

        # 5 - click and write ..
        pyautogui.click(1349, 431, duration=0.5)
        pyautogui.write(date)
        # 2 - Click and write ... again if necessary
        pyautogui.click(1350, 460, duration=0.5)
        pyautogui.write(home_team)
        # 3 - only click ... if necessary
        pyautogui.click(1355, 495, duration=0.5)
        pyautogui.write(away_team)
        # 1 - ...............
        pyautogui.click(1353, 521, duration=0.5)
        pyautogui.write(team)
        # 0.5 - Click and write ... again if necessary
        pyautogui.click(1355, 552, duration=0.5)
        pyautogui.write(scorer)
        # 3 - only click ... if necessary
        pyautogui.click(1349, 583, duration=0.5)
        pyautogui.write(minute)
        # 0.5 - Click and write ... again if necessary
        pyautogui.click(1351, 611, duration=0.5)
        pyautogui.write(own_goal)
        # 3 - only click ... if necessary
        pyautogui.click(1352, 643, duration=0.5)
        pyautogui.write(penalty)
        # - finalizando cadastro:
        pyautogui.click(1169, 708, duration=0.5)
        pyautogui.click(1370, 706, duration=0.5)
        sleep(0.5)

# Aguarda a finalização do thread
thread.join()
