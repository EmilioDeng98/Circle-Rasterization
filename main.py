# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from PIL import Image


def circle(radius):
    "Bresenham complete circle algorithm in Python"
    # init vars
    switch = 3 - (2 * radius)
    points = set()
    x = 0
    y = radius
    # first quarter/octant starts clockwise at 12 o'clock
    while x <= y:
        # first quarter first octant
        points.add((x, -y))
        # first quarter 2nd octant
        points.add((y, -x))
        # second quarter 3rd octant
        points.add((y, x))
        # second quarter 4.octant
        points.add((x, y))
        # third quarter 5.octant
        points.add((-x, y))
        # third quarter 6.octant
        points.add((-y, x))
        # fourth quarter 7.octant
        points.add((-y, -x))
        # fourth quarter 8.octant
        points.add((-x, -y))
        if switch < 0:
            switch = switch + (4 * x) + 6
        else:
            switch = switch + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1
    return points


def fillCircle(circle, center, color):
    stack = [center]
    while len(stack) > 0:
        point = stack.pop()
        if circle[point[0], point[1]] == color:
            continue
        circle[point[0], point[1]] = color
        # Four Direction Filling
        if circle[point[0] + 1, point[1]] != color:
            stack.append([point[0] + 1, point[1]])
        if circle[point[0] - 1, point[1]] != color:
            stack.append([point[0] - 1, point[1]])
        if circle[point[0], point[1] - 1] != color:
            stack.append([point[0], point[1] - 1])
        if circle[point[0], point[1] + 1] != color:
            stack.append([point[0], point[1] + 1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    img = Image.new('RGB', (400, 400))
    pixels = img.load()
    radius = 100
    center = [200, 200]
    topPoint = [center[0] + radius, center[1]]
    print(topPoint)
    circle = circle(100)
    for item in iter(circle):
        pixels[center[0] + item[0], center[1] + item[1]] = (255, 0, 0)
    fillCircle(pixels, center, (255, 0, 0))
    img.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
