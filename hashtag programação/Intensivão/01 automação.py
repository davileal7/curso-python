import pyautogui as pa
import time

pa.moveTo(x=933, y=1059, duration=1)
pa.click(x=933, y=1059)
time.sleep(1)
pa.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pa.press('enter')

time.sleep(5)
pa.position()
print(pa.position())








