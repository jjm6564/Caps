
#----------------
import pyautogui
import time
import text
import json
#----------------

with open(r'locate.json','r')as f:
    json_data = json.load(f)

dirLoacte  = json_data['Pinata']['dirLocate']
#uploadBtn = json_data['Pinata']['uploadButtonForDir']
uploadBtn = json_data['Pinata']['uploadbtn']

dirPath = r'C:/Users/mvr/Desktop/JM/NFT/'

def uploadPinataAutogui():
    time.sleep(1)
    pyautogui.moveTo(dirLoacte)
    print(pyautogui.position())
    pyautogui.click()
    pyautogui.typewrite(dirPath+text.username,interval=0.03)
    pyautogui.hotkey('ENTER')
    #---movedir

    pyautogui.moveTo(uploadBtn)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('LEFT')
    pyautogui.hotkey('ENTER')