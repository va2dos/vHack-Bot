from enum import IntEnum
import os
import time
from BlueHackWindow import HOME
from Macros.Mining import NC_Mining
from Macros.Botnet import Farm_Botnet
from Macros.Rewards import WheelSpins, SlotSpins
from Macros.Track import Track_Nouse
from Macros.Network import Farm_Network
from Macros.Terminal import Farm_Terminal
from Macros.Banking import Farm_Wallets
from Utils import get_config

config = get_config()

class MenuItems(IntEnum):
    AUTO = 0
    NC = 1
    NETWORK = 2
    TERMINAL = 3
    BOTNET = 4
    SPIN = 5
    WHEEL = 6
    BANK = 7
    DEBUG_MOUSE = 8
    QUIT = 9

def main():
    while True:
        try:
            # Go to Home at start
            HOME()

            # Print menu
            print('Type the number of the option you want.')
            for item in iter(MenuItems) :
                print(' [{}] {}'.format(item.value, item.name))

            # Wait for Script Pick
            user_input = input('What would you like to do? ')
            if not user_input.isdigit() or not int(user_input) in iter(MenuItems) :
                os.system('cls||clear')
                print('Not a valid option.')
                continue
            
            menuItem = MenuItems(int(user_input))
            print('CLTR-C at any moment to return to main menu')
            print('starting: ' + menuItem.name + '\n')

            match menuItem:
                case MenuItems.AUTO:
                    #Every look taps ~ 15 minutes
                    # 4x 75 Target = 300 for dailys
                    for i in range(1, 4):
                        HOME()
                        WheelSpins()
                        HOME()
                        SlotSpins()
                        HOME()
                        Farm_Wallets()
                        HOME()
                        Farm_Botnet()
                        HOME()
                        Farm_Network()
                        HOME()
                        NC_Mining(50) # 5 Minutes
                        Farm_Terminal()
                        HOME()                       
                        NC_Mining(10)

                case MenuItems.NC:
                    NC_Mining(10)
                case MenuItems.BOTNET:
                    Farm_Botnet()
                case MenuItems.SPIN:
                    WheelSpins()
                case MenuItems.WHEEL:
                    SlotSpins()
                case MenuItems.NETWORK:
                    Farm_Network()
                case MenuItems.TERMINAL:
                    Farm_Terminal()
                case MenuItems.BANK:
                    Farm_Wallets()
                case MenuItems.DEBUG_MOUSE:
                    Track_Nouse()
                case MenuItems.QUIT:
                    print('Closing...')
                    exit(0)
                    
        except KeyboardInterrupt:
            continue
        
        except Exception as e: 
            print(e)
            exit(1)

if __name__ == '__main__':
    main()