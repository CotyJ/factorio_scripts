# Packages
import keyboard
import mouse
import time
import pandas as pd

# Data
from preset_1 import preset1 as preset
from items import items
# from create_coordinates import create_coordinates


# Variables --------------------------------------------
  # Item boxes are 40x40 including spacing
item_box = 40

  # Starting position on my laptop screen
starting_position = [776,  1048]

  # Filter starting pos
filter_start_pos =  [804, 670]
# mouse.move(*filter_start_pos)

  # timing delay
delay = .1

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

# ++++++++++++++++++++ MAIN LOOP +++++++++++++++++++++++++++++
for key in hotbar_coordinates:

  hbX = hotbar_coordinates[key][0]
  hbY = hotbar_coordinates[key][1]
  # print(hbX, hbY)
  # print(key)

  # Move mouse to position on hotbar---------------------------
  mouse.move(hbX, hbY)        # --------------ACTION
  print("moving to hotbar", hbX, hbY)
  mouse.click(button='left')  # --------------ACTION
  time.sleep(delay*2)

  """
  keyboard.press('escape')    # --------------ACTION
  time.sleep(delay*2)
  keyboard.release('escape')  # --------------ACTION
  time.sleep(delay*2)
  """

  # Move mouse to appropriate tab and click--------------------
  # Move mouse to item and click
  item =           preset[key]      # Item key name
  item_fancy =     items[item][0]   # Item Full Name
  tab =            items[item][1]   # Item tab name
  itemX_offset =   int(items[item][2] * 40)  #
  itemY_offset =   int(items[item][3] * 40)  #
  hotbar_offsetX = (int(key.split('-')[0]) - 1) *  40
  hotbar_offsetY = (int(key.split('-')[1]) - 1) * -40
  moveX =          itemX_offset + filter_start_pos[0] - hotbar_offsetX
  moveY =          itemY_offset + filter_start_pos[1] - hotbar_offsetY

  print("item:",   item)
  print("Item:",   item_fancy)
  print("Tab:",    tab)
  print("ItemX:",  items[item][2], "ItemY:", items[item][3])
  print("Offset from hotbar position X:", hotbar_offsetX)
  print("Offset from hotbar position Y:", hotbar_offsetY)
  print("Item X offset:", itemX_offset)
  print("Item Y offset:", itemY_offset)

  time.sleep(delay)

  # Move mouse to item and click
  mouse.move(moveX, moveY)     # --------------ACTION
  print("Move Mouse to Item:", moveX, moveY)
  time.sleep(delay)
  mouse.click(button='left')

  # hotbar 1-1 should be clicked at about 776, 1052 WORKS
  # roboport   should be clicked at about 1174, 930 OFF

  """
  keyboard.press('escape')    # --------------ACTION
  time.sleep(delay)
  keyboard.release('escape')  # --------------ACTION
  time.sleep(delay*3)
  """

  print('\n')
  break;

print("\nDone")
