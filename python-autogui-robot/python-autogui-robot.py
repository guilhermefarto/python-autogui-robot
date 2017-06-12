# coding: utf-8
import pyautogui, time

# time.sleep(2)

# add delays after all of PyAutoGUI's functions by setting the pyautogui.PAUSE variable to a float or integer value of the number of seconds to pause
# by default, the pause is set to 0.1 seconds
pyautogui.PAUSE = 2.5

# screen size (width, height)
print(pyautogui.size())

# actual mouse position (x, y)
print(pyautogui.position())

# move mouse to position (x, y)
pyautogui.moveTo(100, 100, duration=0.25)

# move mouse to relative position (+/- x, +/- y)
pyautogui.moveRel(100, 0, duration=0.25)

# simulate mouse click at position (x, y) with left mouse button (by default)
pyautogui.click(10, 5)

# simulate mouse click at position (x, y) with custom mouse button ('left', 'middle', or 'right')
pyautogui.click(10, 5, button='right')

# simulate mouse click with left button
pyautogui.click()

# simulate mouse click with middle button
pyautogui.middleClick()

# simulate mouse click with right button
pyautogui.rightClick()

# simulate double click (with left button)
pyautogui.doubleClick()

# press the left mouse button
pyautogui.mouseDown()
# waits 2 seconds
time.sleep(2)
# release the left mouse button
pyautogui.mouseUp()

# simulate mouse dragging (moving the mouse while holding down one of the mouse buttons) at positions (x, y)
pyautogui.dragTo(100, 100, duration=0.25)

# simulate mouse dragging (moving the mouse while holding down one of the mouse buttons) at relative positions (+/- x, +/- y)
pyautogui.dragRel(100, 0, duration=0.25)

# scrolls mouse up
pyautogui.scroll(200)

# scrolls mouse down
pyautogui.scroll(-200)

# return an Image object (see the Pillow or PIL module)
im = pyautogui.screenshot()

# returns the pixel color (RGB tuple)
im.getpixel((0, 0))

# checks if the pixel color (RGB tuple) is equal to last method argument (true/false)
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144), tolerance=10)

# inline example
pyautogui.screenshot().getpixel((x, y))

# takes and saves the screenshot in 'screen.png' file (same .py directory)
pyautogui.screenshot('screen.png')
# takes and saves the screenshot in 'screen.png' file (custom directory)
pyautogui.screenshot('C:/screenshots/screen.png')

# four-integer tuple with x-coordinate of the left edge, the y-coordinate of the top edge, the width, and the height for the first place on the screen the image was found
pos = pyautogui.locateOnScreen('button.png') # e.g., pbrush application
# move mouse to center position (x, y) for the first place on the screen the image was found
pyautogui.moveTo(pos[0] + (pos[2] / 2), pos[1] + (pos[3] / 2))

# locates all objets on screen
list(pyautogui.locateAllOnScreen('submit.png'))

# locates first centered place on the screen the image was found
pos = pyautogui.locateCenterOnScreen('button.png') # XY coordinates of the middle of where the image is found on the screen

# coordinates (x, y) at the center of this region for argument (four-integer tuple with x, y, width, and height)
print(pyautogui.center((714, 48, 58, 69)))

# prints out the argument (as String) instantly
pyautogui.typewrite('Hello, my name\'s Guilherme.')
# prints out the argument (as String) with a quarter second delay after each character
pyautogui.typewrite('Hello, my name\'s Guilherme.', interval=0.25)
# simulates multiple keys pressing with a list of arguments (as Strings) and/or Keyboards keys
# full list of key names is in pyautogui.KEYBOARD_KEYS (http://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.5)

# prints all Keyboard keys constants
print(pyautogui.KEYBOARD_KEYS)

# simulate key press
pyautogui.press('enter')
# simulate multiple keys press
pyautogui.press(['enter', 'f1'])

# simulate key press (with commands, e.g., shift, ctrl, and others)
pyautogui.keyDown('shift')
pyautogui.press('a')
pyautogui.keyUp('shift')

# simulate hotkeys or keyboard shortcuts convenient
pyautogui.hotkey('shift', 'a')

# another example
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')

# another example
pyautogui.hotkey('ctrl', 'a')