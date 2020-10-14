import pyautogui, time

choice = input("""
$Created by i1470s#0396$

Made for brain dead skids with love <3

[1] How it works this explains everything!
[2] Spammer

Enter a option: """)


if choice == '1':
    print("""Hey Skid! this is a very simple program! if you want to change what the spammer sends 
go to libs/text.txt and change the 10000 lines of pp poo poo to what ever you want!""")
    time.sleep(100000)

elif choice == '2':
    print("Welcome your a dick for using this btw") 
    time.sleep(2)
    print("Starting spam in 10 seconds") 
    time.sleep(10)
    print("Spamming thy skid :P")
    f = open("./libs/text.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        time.sleep(.2)
        pyautogui.press("enter")