# Internal Functions

# The following two functions get user input for datapoints and store the X,Y pairs as tuples in a list.
# The user continues to add as many datapoints as they want. When they are done they can finish entering
# datapoints by entering [Y]es when prompted.
datapoints = []
def make_point(x, y):
  return (x,y)


def add_datapoints():
  done = False
  while done == False:
    x = int(input("X value: "))
    y = int(input("Y value: "))
    datapoints.append(make_point(x, y))
    ask_done = input(f"Your datapoints so far: {datapoints}. Are you done entering points? [Y]es or [N]o: ")
    if ask_done.upper() == 'Y':
      done = True
    elif ask_done.upper() == 'N':
      done = False
    else:
      print("Please enter valid answer. We will assume that you are NOT done entering points")
      done = False



# The following three functions excecute the maths required to calculate the amount of error for a given dataset.
def get_y(m, b, x):
  y_value = m * x + b
  return y_value


def calculate_error(m, b, point):
  x_point, y_point = point
  y = get_y(m, b, x_point)
  distance = abs(y - y_point)
  return distance
 

def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error


# Main Excecution
# The user is asked for input as described above
add_datapoints()


# Creates lists for every possible value for the slope(m) and the y-intercept(b) 
# between -100 and 100 (inclusive of 100) going up in incriments of 0.1
possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-100, 101)]

# The following block of code is responsible for iterating through every single possibility for
# slope(m) and y-intercept(b), and finding the line that produces the least error
smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m, b, datapoints) < smallest_error:
            best_m = m
            best_b = b
            smallest_error = calculate_all_error(m, b, datapoints)


# Finally, the synthisised data is output in a user friendly format
print(f"""
The best linear regression line for the datapoints {datapoints} 
has a slope(m) of {best_m}, 
a y-intercept(b) of {best_b}, 
and produces an error value of just {smallest_error}
You can graph this line using it's slope(m) and y-intercept(b), 
and you can represent it as an equation with Y=Mx + B. In this case, that's Y={best_m}x + {best_b}
where Y and x represent any given point on the line.
"""
)
# Thank you for using LinearRegress, a sub-program of MathKit. Please use and distribute ethically.
# you can read more about this in the file labled README.MD within this program folder
# Written and developed in Python by Eli Hatton for Zinc Softwares 2020
