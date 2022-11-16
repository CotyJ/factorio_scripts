import mouse
import time
import keyboard
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
# print(coordinates)

# Moves mouse over all hotkey positions
for key in coordinates:
  mouse.move(*coordinates[key])

  # Reset buttons
  # mouse.click(button='middle')
  # keyboard.press_and_release('escape')
  # keyboard.press_and_release('escape')

  print(key, *coordinates[key])
  time.sleep(.02)


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


# build the dictionary for coordinates.py
rows = 10
columns = 4
# coords = create_coordinates(rows, columns)

# Dataframe to export as CSV
# coords_df = pd.DataFrame(coords)
# coords_df.to_csv('coordinates.csv')
