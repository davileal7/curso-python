import pyautogui
#import pyperclip
import time

#acessar meu canal youtube
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write('https://www.youtube.com/')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(x=1857, y=99, duration=1)
pyautogui.click(x=1857, y=99)
time.sleep(1)
pyautogui.moveTo(x=1635, y=242, duration=1)
pyautogui.click(x=1635, y=242)

pyautogui.position()
print(pyautogui.position())
