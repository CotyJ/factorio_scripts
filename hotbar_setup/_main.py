# Packages
import keyboard
import mouse
import time
import pandas as pd

# Data
from preset_1 import preset1 as preset
from items import items
# from create_coordinates import create_coordinates


# Variables _________________________________________
  # Item boxes are 40x40 including spacing
item_box = 40

  # Starting position on my laptop screen
starting_position = [776,  1048]

  # Filter starting pos
filter_start_pos =  [804, 670]

  # timing delay
delay = .05

  # tab locations starting at 4-1
tabs = {
  "logistics":     [824, 600],
  "production":    [932, 600],
  "intermediates": [1040, 600],
  "combat":        [1138, 600],
}

# END Variables _____________________________________


# Import Coordinates file
hotbar_coordinates = pd.read_csv('hotbar_coordinates.csv')  # Imports as a Dataframe

# print(items)

# ++++++++++++++++++++ MAIN LOOP ++++++++++++++++++++
for key in hotbar_coordinates:

  hbX = hotbar_coordinates[key][0]
  hbY = hotbar_coordinates[key][1]
  # print(key)

  # Move mouse to position on hotbar
  # mouse.move(hbX, hbY)
  # mouse.click(button='left')
  # time.sleep(delay * 0.5)
  # keyboard.press_and_release('escape')
  # time.sleep(delay)

  # Move mouse to appropriate tab and click
  it = preset[key]
  # print(it, type(it))
  item = items[it]
  # print(item)

  tab_offset = item[2] + (40 * ) + 0, item[3] + (40 * )
  print(tab_offset)



print("\nDone")
