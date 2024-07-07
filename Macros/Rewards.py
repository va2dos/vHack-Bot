import time
from random import randrange, uniform
import pyautogui as pag
from BlueHackWindow import GetElement, check_connection
pag.FAILSAFE = True

BlueHackImages = {
    'wheel_confirm': ['images/wheel_confirm.png', 'Center Wheel'],
    'wheel_no_spins': ['images/wheel_no_spins.png', 'WheelNo Spins'],
    'slot_no_spins': ['images/slot_no_spins.png', 'No Spins']
}

MouseCords = {
    'Wheel Icon': [802, 982],
    'Slot Icon': [894, 982],
    'Slot Spin': [946, 893],
}

def click_wait(x, y, clicks):
    count = 0
    while count < randrange(clicks-1)+1:
        cX = randrange(10) - 5 + x
        cY = randrange(10) - 5 + y
        pag.click(cX, cY)
        time.sleep(uniform(0.53, 1.28))
        count += 1

def WheelSpins():
    # Click on the wheel icon
    pag.click(MouseCords['Wheel Icon'][0], MouseCords['Wheel Icon'][1])
    time.sleep(.3)
    
    try:
        while check_connection(0):

            no_spint, (_,_) = GetElement(BlueHackImages['wheel_no_spins'][0], 0.99) # SPINS: 8, trigger 98% OK
            if no_spint == True:
                return

            # Check for the confirmation button to spin the wheel
            wheel_confirm, (confirm_x, confirm_y) = GetElement(BlueHackImages['wheel_confirm'][0], 0.8)
            if wheel_confirm == False:
                return

            click_wait(confirm_x, confirm_y, 3)
            time.sleep(uniform(0.8, 1.5))

    except KeyboardInterrupt:
        pass

def SlotSpins():
    # Click on the Slot icon
    pag.click(MouseCords['Slot Icon'][0], MouseCords['Slot Icon'][1])
    time.sleep(.3)

    try:
        while True:
            no_spins, (_, _) = GetElement(BlueHackImages['slot_no_spins'][0], 0.8)
            if no_spins == True:
                return

            click_wait(MouseCords['Slot Spin'][0], MouseCords['Slot Spin'][1], 3)
            time.sleep(uniform(0.8, 1.5))

    except KeyboardInterrupt:
        pass