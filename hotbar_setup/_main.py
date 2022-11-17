# Packages
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
logistics_start = [824, 600]
production_start = [932, 600]
intermediates_start = [1040, 600]
combat_start = [1138, 600]

# END Variables _____________________________________


# Import Coordinates file
hotbar_coordinates = pd.read_csv('hotbar_coordinates.csv') # Imports as a Dataframe


# ++++++++++++++++++++ MAIN LOOP ++++++++++++++++++++
for key in hotbar_coordinates:
  # Reset buttons here if needed
  """
  mouse.click(button='middle')
  keyboard.press_and_release('escape')
  keyboard.press_and_release('escape')
  """
  # Move mouse to hotbar location and click---- DONE

  # Move mouse to position on hotbar, then click
  mouse.move(hotbar_coordinates[key][0], hotbar_coordinates[key][1])
  # mouse.click(button='left')
  time.sleep(delay)

  # Move mouse to appropriate tab and click
  mouse.move()

# WIP
"""
  # mouse.click(button='left')
  # offset_l =hotbar_coordinates[key][2]
  # print(offset_l)
  # offsetX = offset_l[1:].split(',')[:-1]
  # offsetX = int("Offset:", offsetX[0][0])

  # offsetY = ???
  # offsetY = offsetY[0]

  # print("OffsetX:", offsetX, type(offsetX))
  # print("OffsetY:", offsetY, type(offsetY))
  # print('')

  # offsetX = offset[0]
  # offsetY = offset[1]
  # print(offsetX, offsetY)

  # Move mouse to tab and click----------------
  # Move mouse to item position, offset by hotbar location
  # mouse.move(1, 1)
    # mouse.click(button='left')



  # Move mouse to item and click--------------
    # mouse.click(button='left')


  # print(key, *hotbar_coordinates[key])
  # time.sleep(delay)
"""
#_____________________________________________________


# Move mouse to bottom left hotbar
# mouse.move(*starting_position)
# mouse.click(button='left')
# time.sleep(.4)

# move mouse to logistics tab and click
# mouse.move(*logistics_start)
# mouse.click(button='left')
# time.sleep(.4)

# mouse.move(*filter_start_pos)

# effectively the offset for each item
small_box_dims = 40

time.sleep(delay)
# mouse.move(*start_pos)

# position of given item
# row_location = [804 + (columns * 40), 670 + (rows * 40)]


# Pipe and cliff example
"""
# pipe =  [4, 3]
# cliff = [6, 8]
# pipe_loc =  [start_pos[0] + (small_box_dims * pipe[0]),  start_pos[1] + (small_box_dims * pipe[1])]
# cliff_loc = [start_pos[0] + (small_box_dims * cliff[0]), start_pos[1] + (small_box_dims * cliff[1])]
"""

# item location
# starting position        + the offset of the item in menu            + offset due to hotbar key start
# item_loc = [start_pos[0] + (small_box_dims * item[0]),  start_pos[1] + (small_box_dims * item[1])]


# Wall example *****************************************
"""
wall = items["wall"]
# print("Wall:", wall, "\n")
wall_hotbar_location = ["0-0"]

# print(f"Start at {wall_hotbar_location[0][0]}, {wall_hotbar_location[0][2]}")
mouse.move(*combat_start)

# mouse.move(wall_hotbar_location[0][0], wall_hotbar_location[0][2])
mouse.click(button="left")
print("Click!")
time.sleep(1)

print("Move to combat:", combat_start)
mouse.move((combat_start[0] + (int(wall_hotbar_location[0][0]) * 40)), (combat_start[1] + (int(wall_hotbar_location[0][2]) * 40)))
# mouse.click(button="left")
time.sleep(1)

# x and y below will be replaced by key[0] and key[2]
# so it will parse the string like "3-0"
# print(wall[2][0], wall[2][1])
# mouse.move(wall[2][0], wall[2][1])
time.sleep(1)
"""
"""
print("Name:", wall[0])
print("Tab: ", wall[1])
print("Row, Col:", wall[2])
print("Combat tab starting position: ", combat_start)
"""

# END Wall example ************************************



# Old procedural
"""
time.sleep(.5)
print("\n Click on hotbar 3-1 ( X = 3, Y = 1)")
mouse.move(*hotbar_coordinates["3-1"])

time.sleep(.5)
print("\n Click on hotbar 1-1")
mouse.move(*hotbar_coordinates["1-1"])

time.sleep(.5)
print("\n Click on hotbar 3-4")
mouse.move(*hotbar_coordinates["3-4"])
"""

# Old calcs
"""
wall_3_3_loc =
[
start_pos[0] + (small_box_dims * items["wall"][3][0]),
start_pos[1] + (small_box_dims * items["wall"][3][1])
 ]

mouse.move(*wall_3_3_loc)
time.sleep(delay)
mouse.move(*cliff_loc)
time.sleep(delay)
"""


print("Done")


# Export Function______________________________________
"""
# build the dictionary for coordinates.py
rows = 10
columns = 4
coords = create_coordinates(rows, columns)

# Dataframe to export as CSV
coords_df = pd.DataFrame(coords)
coords_df.to_csv('hotbar_coordinates.csv')
"""
