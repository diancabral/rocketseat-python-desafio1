# Obs: Sim, eu fiz isso :)

from math import floor

def drawBox(text: list, center=True, paddingY=True):
  BOX_COLS = 60

  if paddingY:
    text.insert(0, "")
    text.append("")

  print(f"┌{'-' * BOX_COLS}┐")

  for value in text:
    chars = len(value)
    diference = (BOX_COLS - chars) / 2
    spaces = floor(diference)
    if center:
      print(f"|{' ' * spaces}{value}{(' ' * (spaces - (1 if diference.is_integer() else 0)))} |")
    else:
      print(f"| {value}{(' ' * ((spaces * 2) - (2 if diference.is_integer() else 1)))} |")

  print(f"└{'-' * BOX_COLS}┘\n")
