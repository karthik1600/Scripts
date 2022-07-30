
import pyautogui
import time
 
time.sleep(5)
 
for line in open("wififix.txt", "r"):
 
    pyautogui.typewrite(line)
    time.sleep(2)
    pyautogui.press("enter")


