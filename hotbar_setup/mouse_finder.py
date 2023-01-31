# Watches the mouse and prints coordinates
import time
import mouse
from items import items

def map_mouse(number):
  time.sleep(.5)
  for num in range(number):
    pos = mouse.get_position()
    print(pos)
    time.sleep(.5)


time.sleep(1)
map_mouse(12)

# mouse.move (50, 560)
time.sleep(1)

# mouse.move (465, 420)

