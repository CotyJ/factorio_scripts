# creates a coordinates dictionary with the below schema
#    { "col-row": [X, Y]        col, row }
# ex { "1-1":     [776, 1048] , 1,   1   }
# putting a list inside of a list for the property converted them to a string

def create_coordinates(row, col):
  rows_start = 1
  columns_start = 1
  dic = {}

  row_list = []
  col_list = []

  while rows_start <= row:
    row_list.append(rows_start)
    rows_start += 1

  while columns_start <= col:
    col_list.append(columns_start)
    columns_start += 1

  for row in row_list:
    for col in col_list:
      newstr = str(row) + "-" + str(col)

      # here
      starting_position = [776, 1048]
      print("col ", int(str(row)))
      # if first half (left 5)
      if int(str(row)) <= 5:
        print("less than equals 5")
        dic[newstr] = [starting_position[0] + (40 * (row - 1)), starting_position[1] - (40 * (col - 1)), row, col]
      else:
        print("greater than 5")
        dic[newstr] = [starting_position[0] + (40 * (row - 1)) + 4, starting_position[1] - (40 * (col - 1)), row, col]


      # if second half (right 5)

  # How to calculate AND insert the correct values?
  # if there is one row, then 1-1 is  [776,  1048]
  # if there are four,   then 4-1 is  [776,  1048]
  # and offsets the rest, now 1-1 is  [776,  928]
  print(dic)
  return dic
