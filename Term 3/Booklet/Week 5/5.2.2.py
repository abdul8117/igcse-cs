# linear search
"""
SET nameTarget TO <any name>
SET nameList TO <the list of names>
SET isName TO False

WHILE:
  FOR name IN nameList:
    IF name.lower() == nameTarget.lower()
      isName = True
      print(name)
      break loop
    ELSE:
      conitnue loop
  IF isName == False:
  SEND "name not found" TO DISPLAY
UNTIL isName == False
"""

name = 'henry'
name_list = ['Anya', 'Max', 'Erik', 'William', 'David', 'Shirley', 'Cheryl', 'Ben', 'Rosie', 'Henry', 'Georgina']
is_name = False

while is_name == False:
  for i in name_list:
    if name.lower() == i.lower():
      is_name = True
      print(is_name)
      print(i)
      break
    else:
      continue
  if is_name == False:
    print(is_name, '-', f"the name, '{name}', was not found") 
    break