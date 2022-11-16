import mouse
import time
import keyboard
from items import items
from create_coordinates import create_coordinates
import pandas as pd

# Item boxes are 40x40 including spacing
item_box = 40

# Starting position on my laptop screen
starting_position = [776,  1048]


# Import Coordinates file
hotbar_coordinates = pd.read_csv('hotbar_coordinates.csv')
# print(coordinates)

# Moves mouse over all hotkey positions
for key in hotbar_coordinates:
  mouse.move(*hotbar_coordinates[key])
  # Reset buttons
  # mouse.click(button='middle')
  # keyboard.press_and_release('escape')
  # keyboard.press_and_release('escape')
  print(key, *hotbar_coordinates[key])
  time.sleep(.02)


# build the dictionary for coordinates.py
rows = 10
columns = 4
# coords = create_coordinates(rows, columns)

# Dataframe to export as CSV
# coords_df = pd.DataFrame(coords)
# coords_df.to_csv('hotbar_coordinates.csv')
