# creates a coordinates dictionary with the below schema
#  { "col-row": [0, 0] }
# ex { "1-1":   [0, 0 }

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
      newstr1 = str(row)
      newstr2 = str(col)
      newstr = newstr1 + "-" + newstr2
      dic[newstr] = [0, 0]
  return dic
