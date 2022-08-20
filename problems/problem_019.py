# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of the rectangle
#   rect_y: The bottom of the rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):

    """Evaluate x and y within bounds"""

    x_check = (x >= rect_x) and (x <= (rect_x + rect_width))
    y_check = (y >= rect_y) and (y <= (rect_y + rect_height))

    return x_check and y_check


# Initialize var
x = 12
y = 10
rect_x = 2
rect_y = 4
rect_width = 100
rect_height = 80

# Invoke and print
print(is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height))
