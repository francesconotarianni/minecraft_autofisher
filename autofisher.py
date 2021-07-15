import time
from PIL import ImageGrab
from PIL import Image
from plyer import notification
import mss
import pytesseract
import mouse
import keyboard

"""An automatic, future-proof minecraft autofisher that uses text-from-image recognition"""

# create the global functions to use afterwards
box = None


def main():
    # Let's create a notification to see if everything's working alright and to give instructions about the script
    immagine = 'Minecraft.ico'
    notification.notify(title='Autofisher',
                        message='Press "z" to start the script, long press "x" to stop the script', timeout=5,
                        app_icon=immagine)

    # Isolate the part of the screen that interests us, using percentage values to prevent errors at different
    # resolutions
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        left = monitor['left'] + monitor['width'] * 0.7
        top = monitor['top']
        right = monitor['width']
        lower = top + monitor['height']
        global box
        box = (left, top, right, lower)

    # uncomment this to see the coordinates of the screen
    # print(box)

    keyboard.wait('z')
    # uncomment this to see if it's working
    # print("Let's go then!")
    image_searcher()


def image_searcher():
    for _ in iter(int, 1):
        # uncomment this to make it go full speed
        # time.sleep(2)
        # checks if the 'x' key is pressed down. If so, terminates the program
        if keyboard.is_pressed('x'):
            break

        # takes screenshots
        lato_schermo = ImageGrab.grab(box)
        # uncomment this part to check what part of the screen is screenshotted
        # Image._show(lato_schermo)

        # search for text in the screenshot
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\franc\Desktop\Desktop\File download vari\Pytesseract\tesseract.exe'  # nopep8
        content = pytesseract.image_to_string(lato_schermo)
        # uncomment this part to see if it works
        # print(content)

        stringa = "Fishing Bobber splashes"  # The string to search for

        if stringa in content:  # check if the string of the sound the bobber makes in minecraft is on the screen
            # uncomment this part to see if it's working
            # print("Found it!")  # TODO ricommenta tutto
            mouse.press(button='right')  # retrieve the bobber with the catch
            mouse.release(button='right')
            time.sleep(1)
            mouse.press(button='right')  # recast the bobber with the catch
            mouse.release(button='right')
        else:
            # uncomment this part to check if it's working
            # print("Nothing here")
            continue


main()
