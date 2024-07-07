import time
import pyautogui as pag
from enum import Enum
from random import uniform, randrange
from BlueHackWindow import BlueHackImages, GetElement, check_connection, MouseCords
pag.FAILSAFE = True

BLOCK_SIZE = 70
MOVE_TWEEN = pag.easeInElastic

class Moves(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

CurrentQuadrant = 1
# 1 2 3
# 4 5 6

# quandrant : [UP, Right, Down, Left]
# 0 = Invalid direction
Quadrants = {
    1: [0, 2, 4, 0],
    2: [0, 3, 5, 1],
    3: [0, 0, 6, 2],
    
    4: [1, 5, 0, 0],
    5: [2, 6, 0, 4],
    6: [3, 0, 0, 5],
}

def drag(direction) :
    global CurrentQuadrant
    # X Range, 680 , 955,  1230, >>> 337, 67px 1 block
    # Y range 215, 610, 1000 >>> 0-1075 > 60px 1 block
    print('Moving {} from Quandrant {}'.format(direction.name, CurrentQuadrant))
    next = Quadrants[CurrentQuadrant]
    match direction:
        case Moves.UP:
            if next[0] == 0: return
            pag.moveTo(955, 500)
            pag.drag(xOffset=0, yOffset=4.5*BLOCK_SIZE, duration=1, button=pag.LEFT, tween=MOVE_TWEEN)
            CurrentQuadrant = next[0]
        case Moves.DOWN:
            if next[2] == 0: return
            pag.moveTo(955, 700)
            pag.drag(xOffset=0, yOffset=-4.5*BLOCK_SIZE, duration=1, button=pag.LEFT, tween=MOVE_TWEEN)
            CurrentQuadrant = next[2]
        case Moves.RIGHT:
            if next[1] == 0: return
            pag.moveTo(1000, 610)
            pag.drag(xOffset=-5*BLOCK_SIZE, yOffset=0, duration=1, button=pag.LEFT, tween=MOVE_TWEEN)
            CurrentQuadrant = next[1]
        case Moves.LEFT:
            if next[3] == 0: return
            pag.moveTo(900, 610)
            pag.drag(xOffset=5*BLOCK_SIZE, yOffset=0, duration=1, button=pag.LEFT, tween=MOVE_TWEEN)
            CurrentQuadrant = next[3]

def wait(t):
    if t < 0: 
        return
    while True:
        if 0 <= t <= 1:
            time.sleep(t)
            break
        else:
            time.sleep(1)
            t -= 1

def click_wait(x, y):
    cX = randrange(10) - 5 + x
    cY = randrange(10) - 5 + y
    pag.click(cX, cY)
    wait(uniform(6.52, 7.28))

def zoomOut():
    zoom_x, zoom_y = MouseCords['Mining Zoom'][0], MouseCords['Mining Zoom'][1]
    pag.mouseDown(x=zoom_x, y=zoom_y)
    wait(3)
    pag.mouseUp()
    wait(0.2)

def NC_Mining(quantity):
    try:
        # Click on Mine App
        mine_x, mine_y = MouseCords['Mine Icon'][0], MouseCords['Mine Icon'][1]
        pag.click(mine_x, mine_y)

        #Zoom out for larger scan
        zoomOut()

        #Goto Top Left, X 5 block, Y 2 block
        pag.moveTo(955, 610)
        pag.drag(xOffset=4.5*BLOCK_SIZE, yOffset=2.8*BLOCK_SIZE, duration=1, button=pag.LEFT, tween=MOVE_TWEEN) 

        counter = _doMine(quantity)
        print('Finish scanning {} blocks'.format( counter ))

        # Go back to main menu
        back_btn_x, back_btn_y = MouseCords['Mining Back'][0], MouseCords['Mining Back'][1]
        pag.click(back_btn_x, back_btn_y)

    except KeyboardInterrupt:
        pass

def _doMine(quantity):
    counter = 0
    while check_connection(0) and counter < quantity:
        # Looks for a block
        found, (x, y) = _check_for_block()
        if found:
            click_wait(x, y)
            counter += 1

        else:
            # Block not found, starts grid scan
            if _scanGrid() == False:
                # No block found else where on the grid
                return counter
            
    return counter

def _check_for_block():
    # Checked for NC Mining block
    found, (x, y) = GetElement(BlueHackImages['nc_block'][0], 0.85)
    if found == True:
        return True, (x, y)
    
    return False, (None, None)

def _scanGrid():
    # Grid is 20 x 20 blocks, 12height x 9 with fit on screen under the header

    while True:

        found, (_,_) = _check_for_block()
        if found == True:
            return True

        # 1 2 3
        # 4 5 6
        # Path 1, 2, 3, 6, 5, 4
        match CurrentQuadrant:    
            case 1:
                drag(Moves.RIGHT)
            case 2:
                drag(Moves.RIGHT)
            case 3:
                drag(Moves.DOWN)
            case 6:
                drag(Moves.LEFT)
            case 5:
                drag(Moves.LEFT)
            case 4:
                # IF allready in 4, no more blocks, 
                # head home and take a break
                return False 
            