
import time
import pyautogui as pag
from random import uniform
from BlueHackWindow import GetElement, check_connection
pag.FAILSAFE = True

BlueHackImages = {
    'wallet_ready': ['images/bank_steal.png'],
}

# Icon 1035, 630
MouseCords = {
    'Bank Icon': [1035, 630],
    'Bank Stash' : [955, 110]
}

def click_wait(x, y):
    pag.click(x, y)
    time.sleep(uniform(0.3, 0.7))

def Farm_Wallets():
    #Target icon, low conficence threshold so may get random selection
    bank_x, bank_y = MouseCords['Bank Icon'][0], MouseCords['Bank Icon'][1]
    click_wait(bank_x, bank_y)

    # Wait 10 seconds, bank might be long to load
    print('waitint 10 seconds to load...')
    time.sleep(10)

    try:
        while check_connection(0): # Continuously attack targets until no more energy

            target_btn_found, (target_x, target_y) = GetElement(BlueHackImages['wallet_ready'][0], 0.98)
            if target_btn_found == False:
                print('No Wallet found, exit')
                break

            click_wait(target_x, target_y)

            #TODO Howto handle transfer failed with img scan ?

    except KeyboardInterrupt:
        pass

    bank_x, bank_y = MouseCords['Bank Stash'][0], MouseCords['Bank Stash'][1]
    click_wait(bank_x, bank_y)

    print('Completed Wallets Farm.\n')