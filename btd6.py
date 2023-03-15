import pyautogui
import time
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


time.sleep(5)

SPEED = .2

monkey_upgrade_locations = {
    "sniper" : {
        "image": "sniper.png",
        "x": 3750,
        "y": 633,
    },
    "village" : {
        "image": "village.png",
        "x": 3635,
        "y": 893,
    },
    "alchemist": {
        "image": "village.png",
        "x": 3744,
        "y": 629,
    }
}

monkey_placements = {
    "sniper" : {
        "x": 3526,
        "y": 499,
    },
    "village" : {
        "x": 3493,
        "y": 579,
    },
    "alchemist": {
        "x": 3510,
        "y": 678,
    }
}
# start btn
startX, startY = 3748,1022

# upgrade locations
path1x = 2258
path1y = 495
path2x = 2259
path2y = 637
path3x = 2252
path3y = 792

def upgradePath1(times):
    pyautogui.moveTo(path1x, path1y, .2)
    for i in range(times):
        pyautogui.click()
        time.sleep(.1)

def upgradePath2(times):
    pyautogui.moveTo(path2x, path2y, .2)
    for i in range(times):
        pyautogui.click()
        time.sleep(.1)

def upgradePath3(times):
    pyautogui.moveTo(path3x, path3y, .2)
    for i in range(times):
        pyautogui.click()
        time.sleep(.1)

def place_monkey(monkey):
    pyautogui.moveTo(monkey_upgrade_locations[monkey]["x"], monkey_upgrade_locations[monkey]["y"], SPEED)
    pyautogui.click()
    pyautogui.moveTo(monkey_placements[monkey]["x"], monkey_placements[monkey]["y"], SPEED)
    pyautogui.click()

def scroll_to_end():
    pyautogui.moveTo(3750,633,.2)

    for i in range(11):
        pyautogui.scroll(-1)

def scroll_to_top():
    pyautogui.moveTo(3750, 633, .2)

    for i in range(11):
        pyautogui.scroll(1)

def upgrade_monkey(monkey, path1, path2, path3):
    pyautogui.moveTo(monkey_placements[monkey]["x"], monkey_placements[monkey]["y"], SPEED)
    pyautogui.click()
    upgradePath1(path1)
    upgradePath2(path2)
    upgradePath3(path3)

# start game
def start_game():
    pyautogui.moveTo(startX, startY, .2)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.click()

def place_all():
    place_sniper_monkey()
    scroll_to_end()
    place_village()
    place_alchemist()
    upgrade_monkey("village", 2,0,2)
    upgrade_monkey("alchemist", 4, 2, 0)
    upgrade_monkey("sniper", 0, 2, 4)
    start_game()

def restart():
    pyautogui.moveTo(3522, 41, .2)
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(2990, 845, .2)
    pyautogui.click()
    pyautogui.moveTo(3066, 730, .2)
    pyautogui.click()
    scroll_to_top()

def reset():
    #click next
    pyautogui.moveTo(2905, 918, .2)
    pyautogui.click()

    #freeplay
    pyautogui.moveTo(3129, 858, .2)
    pyautogui.click()

    restart()

# check for victory
def main():
    while True:
        victory = None
        place_all()
        while not victory:
            time.sleep(15)
            victory = pyautogui.locateOnScreen('victory.png', confidence=0.5)
            levelup = pyautogui.locateOnScreen('levelup.png', confidence = .5)
            if levelup:
                print("LEVELED UP!!!")
                pyautogui.moveTo(3129, 858, .2)
                pyautogui.click()
                time.sleep(.5)
                pyautogui.click()

        print("VICTORY!")
        reset()

main()