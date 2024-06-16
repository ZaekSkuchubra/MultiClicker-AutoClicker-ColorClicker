import pyautogui
import time
import random
from PIL import ImageGrab
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
random_float = random.uniform(0.01, 0.1)
formatted_float = format(random_float, '.5f')
random_sleep_time = float(formatted_float)
def synyna():
    while True:
        x, y = pyautogui.position()
        time.sleep(0.1)
        return x, y
x, y = synyna()
def get_pixel_color(x, y):
    image = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    color = image.getpixel((0, 0))
    return color
def auto_click_until_color_change():
    try:
        while True:
            current_position = pyautogui.position()
            current_color = get_pixel_color(current_position.x, current_position.y)
            pyautogui.click()
            time.sleep(random_sleep_time)
    except KeyboardInterrupt:
        print("Keyboard Interruption")
if __name__ == "__main__":
    print("You have 5 seconds to navigate to your desired window.")
    time.sleep(1)
    print("1", f"   Mouse Position: ({x}, {y})")
    time.sleep(1)
    print("2", r"    /|__|\    Have fun! Made by Za2ek on github.")
    time.sleep(1)
    print("3", r"    |^ ^ |    Entirely OpenSource Project")
    time.sleep(1)
    print("4", r"    | w  |    5 Digit Render is so it doesn't get detected by anti autoclicker protection.")
    time.sleep(1)
    print("5", r"    \ __ /    Check out my other work at my page. Love! ^^ ")
    time.sleep(1)
    print("Go!")
    print("randomised time(5 digit render):" ,random_sleep_time)
    auto_click_until_color_change()