def pr(text, end="\n", color="black", raw="no"):
  color = color.lower()
  if color == "black":
    print(text)
  elif color == "red":
    print("\033[91m {}\033[00m" .format(text), end=end)
  elif color == "green":
    print("\033[92m {}\033[00m" .format(text), end=end)
  elif color == "yellow":
    print("\033[93m {}\033[00m" .format(text), end=end)
  elif color == "lightpurple" or color == "juni":
    print("\033[94m {}\033[00m" .format(text), end=end)
  elif color == "purple" or color == "juniaccent":
    print("\033[95m {}\033[00m" .format(text), end=end)
  elif color == "cyan" or color == "lightblue":
    print("\033[96m {}\033[00m" .format(text), end=end)
  elif color == "lightgray":
    print("\033[97m {}\033[00m" .format(text), end=end)
  else:
    raise NameError("\033[91mThat's not a color!\033[00m")
def pr_list(lst, fancy=True, join=", "):
if fancy:  
  print(join.join(map(str,lst)))
else:
  print(lst)
