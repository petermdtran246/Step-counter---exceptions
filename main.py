def steps_to_miles(steps):
  if steps < 0:
    raise ValueError("Exception: Negative step count entered.")
  return steps / 2000

if __name__ == '__main__':
  while True:
    try:
      steps = int(input())
      break
    except ValueError:
      print("Invalid input. Please enter a whole number of steps.")
  try:
    miles = steps_to_miles(steps)
    print(f"{miles:.2f}")  # Format output with 2 decimal places
  except ValueError:  # Catch ValueError without assigning it to a variable
    print("Exception: Negative step count entered.")