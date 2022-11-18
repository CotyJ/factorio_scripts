# Packages
import mouse
import time
import pandas as pd

# Preset Data
from presets.preset_1 import preset1 as preset

from items import items
# from create_coordinates import create_coordinates  # When creating hotbar CSV


# Variables
item_box = 40
starting_position = [776,  1048]
filter_start_pos =  [804,  670]
delay = .005

tabs = {  # tab locations starting at 4-1
  "logistics":     [824,  600],
  "production":    [932,  600],
  "intermediates": [1040, 600],
  "combat":        [1138, 600],
}

# Import Coordinates file
hotbar_coordinates = pd.read_csv('hotbar_coordinates.csv')

# Move to Resume button
mouse.move(960, 330)        # Move to Resume button
time.sleep(delay)           # DELAY
mouse.click(button='left')
time.sleep(delay)           # DELAY


# MAIN LOOP
for key in hotbar_coordinates:

  itemX_offset   = int(items[preset[key]][2]    * item_box)
  itemY_offset   = int(items[preset[key]][3]    * item_box)
  hotbar_offsetX = (int(key.split('-')[0]) - 1) * item_box
  hotbar_offsetY = (int(key.split('-')[1]) - 1) * item_box
  item_locationX = itemX_offset + filter_start_pos[0] + hotbar_offsetX
  item_locationY = itemY_offset + filter_start_pos[1] - hotbar_offsetY
  tab_offsetX    = tabs[items[preset[key]][1]][0] + hotbar_offsetX
  tab_offsetY    = tabs[items[preset[key]][1]][1] - hotbar_offsetY

  # Move mouse to position on hotbar
  mouse.move(hotbar_coordinates[key][0], hotbar_coordinates[key][1])
  time.sleep(delay)  # DELAY
  mouse.click(button='left')
  time.sleep(delay)  # DELAY

  # Move mouse to appropriate tab and click
  time.sleep(delay)  # DELAY
  mouse.move(tab_offsetX, tab_offsetY)
  time.sleep(delay)  # DELAY
  mouse.click(button='left')
  time.sleep(delay)  # DELAY

  # Move mouse to item and click
  mouse.move(item_locationX, item_locationY)
  time.sleep(delay)  # DELAY
  mouse.click(button='left')
  time.sleep(delay)  # DELAY


print("Done")
# NICE