S = input()

left = int(S[:2])
right = int(S[2:])
if left == 0:
  if 0 < right <= 12:
    print("YYMM")
  else:
    print("NA")
else:
  if left > 12:
    if 0 < right < 13:
      print("YYMM")
    else:
      print("NA")
  elif left > 0:
    if 0 < right < 13:
      print("AMBIGUOUS")
    else:
      print("MMYY")
