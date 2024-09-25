import pyautogui
from time import sleep
# 1 - Click and write ...

# pyautogui.click('cordenadas',duration=2)
# pyautogui.write('input a ser inserido')

# 2 - Click and write ... again if necessary

# pyautogui.click('cordenadas',duration=2)
# pyautogui.write('input a ser inserido')

# 3 - only click ... if necessary

# pyautogui.click('cordenadas',duration=2)

# 4 - extraindo dados de um arquivo (precisa estar na IDE(VSCODE)):
with open('Goal_Scorers.csv','r',encoding='utf-8') as arquivo:
    for linha in arquivo:
        date = linha.split(',')[0]
        home_team = linha.split(',')[1]
        away_team = linha.split(',')[2]
        team = linha.split(',')[3]
        scorer = linha.split(',')[4]
        minute = linha.split(',')[5]
        own_goal = linha.split(',')[6]
        penalty = linha.split(',')[7]
        # 5 - click and write ..  
        pyautogui.click(1349,431,duration=0.1)
        pyautogui.write(date)
        # 2 - Click and write ... again if necessary
        pyautogui.click(1350,460,duration=0.1)
        pyautogui.write(home_team)
        # 3 - only click ... if necessary
        pyautogui.click(1355,495,duration=0.1)
        pyautogui.write(away_team)
        # 1 - ...............
        pyautogui.click(1353,521,duration=0.1)
        pyautogui.write(team)
        # 0.1 - Click and write ... again if necessary
        pyautogui.click(1355,552,duration=0.1)
        pyautogui.write(scorer)
        # 3 - only click ... if necessary
        pyautogui.click(1349,583,duration=0.1)
        pyautogui.write(minute)
                # 0.1 - Click and write ... again if necessary
        pyautogui.click(1351,611,duration=0.1)
        pyautogui.write(own_goal)
        # 3 - only click ... if necessary
        pyautogui.click(1352,643,duration=0.1)
        pyautogui.write(penalty)
        # - finalizando cadastro:
        pyautogui.click(1169,708,duration=0.5)
        pyautogui.click(1370,706,duration=0.5)
        sleep(1)

