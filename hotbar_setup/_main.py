import mouse
import time
from coordinates import coordinates
from items import items

# Item boxes are 40x40 including spacing
item_box = 40
print("Starting Mouse Mapping")


def map_mouse():
  time.sleep(.5)

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)


map_mouse()
