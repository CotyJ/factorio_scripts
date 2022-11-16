import mouse
import time
from items import items
from create_coordinates import create_coordinates
import pandas as pd

# Item boxes are 40x40 including spacing
item_box = 40
# print("Starting Mouse Mapping")

coordinates = pd.read_csv('coordinates.csv')
print(coordinates)

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

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)

  pos = mouse.get_position()
  print(pos)
  time.sleep(.5)


# map_mouse()

time.sleep(.5)

# Starting position, starting with 4-1
# mouse.move(776,  1048)
# time.sleep(.5)
# mouse.move(816,  1048)
# time.sleep(.5)
# mouse.move(856,  1048)
# time.sleep(.5)
# mouse.move(896,  1048)
# time.sleep(.5)
# mouse.move(936,  1048)
# time.sleep(.5)

# 10 pixel gap between left and right half
# mouse.move(980,  1048)
# time.sleep(.5)
# mouse.move(1020, 1048)
# time.sleep(.5)
# mouse.move(1060, 1048)
# time.sleep(.5)
# mouse.move(1100, 1048)
# time.sleep(.5)
# mouse.move(1140, 1048)
# time.sleep(.5)


# build the dictionary for coordinates.py
rows = 10
columns = 4
starting_coords = [776,  1048]
mouse.move(*starting_coords)
coords = create_coordinates(rows, columns)

coords_df = pd.DataFrame(coords)

coords_df.to_csv('coordinates.csv')

print(coords)
print('')
print(coords_df)