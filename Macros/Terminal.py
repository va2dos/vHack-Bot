import time
import pyautogui as pag
from random import uniform
from BlueHackWindow import GetElement, check_connection

BlueHackImages = {
    'term_edit_save': ['images/term_edit_save.png'],
    'term_edit': ['images/term_edit.png'],
    'term_getlog': ['images/term_getlog.png'],
    'term_need_clearlog': ['images/term_need_clearlog.png'],
    'term_over': ['images/term_over.png'],
    'term_ready': ['images/term_ready.png'],
    'term_redeem': ['images/term_redeem.png'],
    'term_transfer': ['images/term_transfer.png'],
}

# Icon @ 1031, 329
# First Target @ 950, 580
MouseCords = {
    'Terminal Icon': [1031, 329],
    'Middle Edit': [960, 340],
    'Save Edit': [960, 1000],
}

# Check for bonus in logs

# Step 2
# To erase Logs
# Get Logs File, Wait 6 seconds, click middle screen, ctrl-a, backspace (to delete), click save

# Step 3
# To Erase tager (Bruteforce Ok), else Repeat Step 2, 3
# Click 3 Second to delete

def click_wait(x, y):
    pag.click(x, y)
    time.sleep(uniform(0.3, 0.7))

def clean_logs():
    edit_btn_found, (edit_x, edit_y) = GetElement(BlueHackImages['term_edit'][0], 0.90)
    if edit_btn_found == False:
        print('cant edit those logs!')
        return
    click_wait(edit_x, edit_y)
    
    #TODO wait for "term_edit_save" button, or "failed" confirmation
    time.sleep(5)

    network_x, network_y = MouseCords['Middle Edit'][0], MouseCords['Middle Edit'][1]
    pag.click(network_x, network_y)
    time.sleep(0.1)
    # Select all text
    pag.hotkey('ctrl', 'a')
    pag.press('backspace')
    time.sleep(0.1)
    pag.write(f' _  _  _  _  __ _  ____  __ \n/ )( \\( \\/ )(  ( \\(  _ \\(  )\n\\ /\\ / )  / /    / )   / )( \n(_/\\_)(__/  \\_)__)(__\\_)(__)\n')
    time.sleep(0.3) # awaiting write

    network_x, network_y = MouseCords['Save Edit'][0], MouseCords['Save Edit'][1]
    click_wait(network_x, network_y)

def Farm_Terminal():
    #Target icon, low conficence threshold so may get random selection
    network_x, network_y = MouseCords['Terminal Icon'][0], MouseCords['Terminal Icon'][1]
    click_wait(network_x, network_y)

    try:
        while check_connection(0): # Continuously attack targets until no more energy

            over_found, (_,_) = GetElement(BlueHackImages['term_over'][0], 0.70)
            if over_found == True:
                print('last target done')
                break

            target_btn_found, (target_x, target_y) = GetElement(BlueHackImages['term_ready'][0], 0.90)
            if target_btn_found == False:
                print('No target ready on screen, waiting...')
                time.sleep(uniform(15, 30))
                continue

            click_wait(target_x + 200, target_y)

            # Step 1 : To Tr.Transfer
            # Click on target, click on button Tr Transfert, if (Tr remainig)
            transfer_btn_found, (transfer_x, transfer_y) = GetElement(BlueHackImages['term_transfer'][0], 0.90)
            if transfer_btn_found == True:
                click_wait(transfer_x, transfer_y)
                # Step 2 : Reload Logs
                _, (getlog_x, getlog_y) = GetElement(BlueHackImages['term_getlog'][0], 0.90)
                click_wait(getlog_x, getlog_y)

            # Check for coupons
            redeem_btn_found, (redeem_x, redeem_y) = GetElement(BlueHackImages['term_redeem'][0], 0.70)
            if redeem_btn_found == True:
                print("Redeem code found!")
                click_wait(redeem_x - 70, redeem_y)

            # Check for leaked Ips
            ip_btn_found, (_,_) = GetElement(BlueHackImages['term_need_clearlog'][0], 0.60)
            if ip_btn_found == True:
                print("Clear Log needed")
                clean_logs()

            # Drop Target, click 2 seconds
            pag.mouseDown(x=target_x + 200, y=target_y)
            time.sleep(uniform(2.1, 2.4))
            pag.mouseUp()

    except KeyboardInterrupt:
        pass

    print('Completed Terminal Farm.\n')

