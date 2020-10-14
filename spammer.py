import pyautogui, time

print("""
$Created by i1470s#0396$

Made for brain dead skids with love <3
""")
print("Starting spam in 10 seconds") 
time.sleep(10)
print("Spamming thy skid :P")
f = open("./libs/text.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(.2)
    pyautogui.press("enter")