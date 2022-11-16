import mouse
import time
from items import items
from create_coordinates import create_coordinates
import pandas as pd

# Item boxes are 40x40 including spacing
item_box = 40
gap = 4

# Starting position on my laptop screen
starting_position = [776,  1048]


# Import Coordinates file
coordinates = pd.read_csv('coordinates.csv')
print(coordinates)

# Moves mouse over all hotkey positions
for key in coordinates:
  mouse.move(*coordinates[key])
  print(key, *coordinates[key])
  time.sleep(.05)


# Watches the mouse and prints coordinates
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
#
# time.sleep(.3)
# starting_coords1 = [776,  1048]
# mouse.move(*starting_coords1)
#
# time.sleep(.3)
# starting_coords2 = [776,  1008]
# mouse.move(*starting_coords2)
#
# time.sleep(.3)
# starting_coords3 = [776,  968]
# mouse.move(*starting_coords3)
#
# time.sleep(.3)
# starting_coords4 = [776,  928]
# mouse.move(*starting_coords4)


# Dataframe to export
coords = create_coordinates(rows, columns)

coords_df = pd.DataFrame(coords)

coords_df.to_csv('coordinates.csv')

# print(coords)
# print('')
# print(coords_df)
