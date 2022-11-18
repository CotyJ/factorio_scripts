# Packages
# import keyboard
import mouse
import time
import pandas as pd

# Preset Data
from presets.preset_1 import preset1 as preset

from items import items
# from create_coordinates import create_coordinates


# Variables --------------------------------------------

item_box = 40                     # Item boxes are 40x40 including spacing
starting_position = [776,  1048]  # Starting position on my laptop screen
filter_start_pos =  [804,  670]    # Filter starting pos
delay = .005                       # timing delay

tabs = {  # tab locations starting at 4-1
  "logistics":     [824,  600],
  "production":    [932,  600],
  "intermediates": [1040, 600],
  "combat":        [1138, 600],
}

# Import Coordinates file
hotbar_coordinates = pd.read_csv('hotbar_coordinates.csv')  # Imports as a Dataframe

# Move to Resume button
time.sleep(delay)           # --------------DELAY
mouse.move(960, 330)        # move to Resume
time.sleep(delay)           # --------------DELAY
mouse.click(button='left')
time.sleep(delay)           # --------------DELAY

# ++++++++++++++++++++++++++++++ MAIN LOOP +++++++++++++++++++++++++++++++++++++++
for key in hotbar_coordinates:

  item =           preset[key]                                          # Item key name
  item_fancy =     items[item][0]                                       # Item Full Name
  tab =            items[item][1]                                       # Item tab name
  itemX_offset =   int(items[item][2] * 40)                             # Item Filter X Offset
  itemY_offset =   int(items[item][3] * 40)                             # Item Filter Y Offset
  hotbar_offsetX = (int(key.split('-')[0]) - 1) * 40                    # Hotbar offset pixels X
  hotbar_offsetY = (int(key.split('-')[1]) - 1) * 40                    # Hotbar offset pixels Y
  item_locationX = itemX_offset + filter_start_pos[0] + hotbar_offsetX  # Item X screen position
  item_locationY = itemY_offset + filter_start_pos[1] - hotbar_offsetY  # Item Y screen position
  tab_position = [tabs[tab][0], tabs[tab][1]]                           # Only used in print_details
  tab_offsetX = tabs[tab][0] + hotbar_offsetX                           #
  tab_offsetY = tabs[tab][1] - hotbar_offsetY                           #

  def print_details():
    print("item:  ", item)
    print("Item:  ", item_fancy)
    print("Tab:   ", tab)
    print("ItemX: ", items[item][2], "ItemY:", items[item][3])
    print("Offset from hotbar position X:", hotbar_offsetX)
    print("Offset from hotbar position Y:", hotbar_offsetY)
    print("Item X offset:", itemX_offset)
    print("Item Y offset:", itemY_offset)
    print("Item Coordinates:", item_locationX, item_locationY)
  # print_details()

  # Move mouse to position on hotbar
  mouse.move(hotbar_coordinates[key][0], hotbar_coordinates[key][1])
  time.sleep(delay)                              # --------------DELAY
  mouse.click(button='left')
  time.sleep(delay)                              # --------------DELAY

  # Move mouse to appropriate tab and click
  time.sleep(delay)                              # --------------DELAY
  mouse.move(tab_offsetX, tab_offsetY)
  time.sleep(delay)                              # --------------DELAY
  mouse.click(button='left')
  time.sleep(delay)                              # --------------DELAY

  # Move mouse to item and click
  mouse.move(item_locationX, item_locationY)
  time.sleep(delay)                              # --------------DELAY
  mouse.click(button='left')
  time.sleep(delay)                              # --------------DELAY


print("Done")
