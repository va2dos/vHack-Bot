import time
import pyautogui as pag
from random import randrange, uniform
from Utils import config
from BlueHackWindow import GetElement, check_connection
pag.FAILSAFE = True

BlueHackImages = {
    'botnet_attack': ['images/botnet_attack.png', 'Botnet Attack'],
    'botnet_back': ['images/botnet_back.png', 'Botnet Back'],
    'botnet_target': ['images/botnet_target.png', 'Botnet Target'],
}

MouseCords = {
    'Botnet Icon': [1176, 322],
    'Botnet Target Icon': [1200, 970],
}

def click_wait(x, y):
    cX = randrange(10) - 5 + x
    cY = randrange(10) - 5 + y
    pag.click(cX, cY)
    time.sleep(uniform(0.8, 1.3))

def Farm_Botnet():
    #Target icon, low conficence threshold so may get random selection
    target = BlueHackImages['botnet_target'][0]
    target_chapter = str(config['Botnet Chapter'])
    botnet_x, botnet_y = MouseCords['Botnet Icon'][0], MouseCords['Botnet Icon'][1]

    click_wait(botnet_x, botnet_y)

    # Click the botnet targets icon
    targetapp_x, targetapp_y = MouseCords['Botnet Target Icon'][0], MouseCords['Botnet Target Icon'][1]

    click_wait(targetapp_x, targetapp_y)

    # Chapter locations and whether scrolling is needed to access them
    Chapters = {
        '1': [944, 478],
        '2': [943, 637],
        '3': [943, 799],
        '4': [943, 561],
        '5': [943, 782]
    }
    chapter_info = Chapters[target_chapter] # Get chapter info

    # Click the specific chapter
    chapt_x, chapt_y = chapter_info[0], chapter_info[1]
    click_wait(chapt_x, chapt_y)

    # Attempt to find and click on the target within the botnet chapter
    target_found, (target_x, target_y) = GetElement(target, 0.8)
    if target_found == False:
        print('Could not find target.')
        return
    
    pag.click(target_x, target_y)
    time.sleep(1)

    try:
        while check_connection(0): # Continuously attack targets until no more energy
    
            # Awaiting Locate to re-render
            time.sleep(.25)

            # Locate the attack button
            attack_btn_found,(attack_x, attack_y) = GetElement(BlueHackImages['botnet_attack'][0], 0.95)
            if attack_btn_found == False:
                # If no attack button found, assume out of energy and return to home
                print('No more energy OR battle took to long!') 
                break
            
            # Awaiting after "attach" modal
            time.sleep(.25)
            # Click on Attack
            click_wait(attack_x, attack_y)

            while True:
                # Wait after Back buton to show
                back_btn_found, (back_x, back_y) = GetElement(BlueHackImages['botnet_back'][0], 0.95)
                time.sleep(1)
                if back_btn_found == True:
                    # Click Back
                    click_wait(back_x, back_y)
                    break

    except KeyboardInterrupt:
        pass

    print('Completed Botnet Farm.')
