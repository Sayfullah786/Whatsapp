import time
import pyautogui
import pywhatkit
from pynput.keyboard import Key, Controller
from mouse import Mouse
from Data import Names,Numbers



mouse = Mouse()


current = time.localtime()
Hour = current[3]
Minute = current[4] + 1

print(Hour)
print(Minute)
pointer = 0

current_time = time.strftime("%H:%M:%S", current)
print(current_time)
while pointer < len(Numbers):


    Logiscool_Promotion_Message = f"Hi {Names[pointer]}, \n \nThank you for showing interest in our Summer Coding camps by Wimbledon Park, \n \nWe at Logiscool would love for you to attend a FREE 1-hour session where we discover which Summer Camp suits your child best. We also have courses resuming in September. Trial can be booked here: \n \nhttps://www.logiscool.com/gb/locations/wimbledon/camp-challenge\n \nOur full day Camp is from 9:30-3:30, half day is 9:30-12:30. We have the following subjects: \n \nHacker Coding - 31 July 2023 to 4 August 2023\n \nIntensive Programming - 7 August 2023 to 11 August 2023\n \nRoblox Game Design  - 14 August 2023 to 18 August 2023\n \nMinecraft - 21 August 2023 to 25 August 2023\n \nThe prices are from £60 for a full-day, £35 for a half-day and/or £175 for the half-day full week or £300 for the full-day full week\n \nKindly let me know if you wanted to book as this is the early bird discount, if you wanted a trial first and can't find the time on the above link then please let me know, \n \nWe look forward to welcoming you to our centre, \n \nJoseph"

    pywhatkit.sendwhatmsg(Numbers[pointer],Logiscool_Promotion_Message,Hour,Minute)

    keyboard = Controller()
    mouse.click()
    time.sleep(10)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print('sent')
    time.sleep(15)
    pyautogui.hotkey('ctrl','w')
    # pyautogui.hotkey('command','w')

    print('Tab Closed')
    print(f'Message sent to {pointer + 1} out of {len(Numbers)}  and the number is to {Names[pointer]}')


    pointer += 1
    Minute += 2
    if Minute >= 58:
        Hour += 1
        Minute = 1
    if Hour == 23 and Minute >= 58:
        Hour = 00
        Minute = 2


    if pointer == len(Numbers):
        new_time = time.localtime()
        new = time.strftime("%H:%M:%S", new_time)
        print(new)
        print('Finished')















