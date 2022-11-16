# Watches the mouse and prints coordinates
import time
import mouse
from items import items

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

time.sleep(1)
# map_mouse()

# tab locations from 4-1
logistics_start = [824, 600]
production_start = [932, 600]
intermediates_start = [1040, 600]
combat_start = [1138, 600]

# test locations
delay = .5

# item locations in select filter
start_pos =  [804, 670]

# effectively the offset for each item
small_box_dims = 40

time.sleep(delay)
mouse.move(*start_pos)

# position of given item
# row_location = [804 + (columns * 38), 670 + (rows * 38)]

# pipe =  [4, 3]
# cliff = [6, 8]

# pipe_loc =  [start_pos[0] + (small_box_dims * pipe[0]),  start_pos[1] + (small_box_dims * pipe[1])]
# cliff_loc = [start_pos[0] + (small_box_dims * cliff[0]), start_pos[1] + (small_box_dims * cliff[1])]

# item location
# starting position        + the offset of the item in menu            + offset due to hotbar key start
# item_loc = [start_pos[0] + (small_box_dims * item[0]),  start_pos[1] + (small_box_dims * item[1])]

print(items["wall"])

wall_3_3_loc = [start_pos[0] + (small_box_dims * items["wall"][3][0]), start_pos[1] + (small_box_dims * items["wall"][3][1])]

mouse.move(*wall_3_3_loc)
# time.sleep(delay)
# mouse.move(*cliff_loc)
# time.sleep(delay)

print("Done")