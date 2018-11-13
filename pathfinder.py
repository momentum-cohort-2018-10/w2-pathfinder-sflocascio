from PIL import Image 

#open file and read it
with open("elevation_small.txt") as text:
    new_text = text.readlines()
#clean list and create a 2d list
new_text = [word.replace('\n', '').strip().split() for word in new_text]
height = [[int(new_text)for new_text in row] for row in new_text]

max_height = (max(height))
min_height = (min(height))
new_max_height = (max(max_height))
new_min_height = (min(min_height))

def elevation_to_color(number):
    """this function converts the elevation data to a color code"""
    color_code = [[round(int(y) - new_min_height) / (new_max_height - new_min_height) * 255 for y in x] for x in number]
    return [[round(n) for n in color_code]for color_code in color_code]

num = (elevation_to_color(height))

#This loop creates a grayscale image using the colorcodes
img = Image.new('RGB', (600, 600))
for y, row in enumerate(num):
    for x, num in enumerate(row):
        img.putpixel((x, y), (num, num, num))
img.save('map.png')


def find_path(height):
    """function to emulate the greedy algorithim, choosing the path with the least elevation increase and returning each choice as an x, y coordinate"""
    y = 300
    x = 0
    starting_location = height[x][y]
    current_location = starting_location

    while x < 601:
        path = [(x, y)]

        up = (height[y+1][x+1])
        middle = (height[y][x+1])
        down = (height[y-1][x+1])
        print(path)

        dif_up = abs(up - current_location)
        dif_middle = abs(middle - current_location)
        dif_down = abs(down - current_location)

        if dif_up < dif_middle and dif_up < dif_down:
                y += 1
                x += 1
                path.append((x, y))                
        elif dif_middle < dif_up and dif_middle < dif_down:
                y += 0
                x += 1
                path.append((x, y))
        elif dif_down < dif_up and dif_down < dif_middle:
                y -= 1
                x += 1
                path.append((x, y))
        elif dif_up == dif_down and dif_up < dif_middle:
                y -= 1
                x += 1
                path.append((x, y))
        elif dif_up == dif_down and dif_up == dif_middle:
                y += 0
                x += 1
                path.append((x, y))
        elif dif_up == dif_middle and dif_middle < dif_down:
                y += 0
                x += 1
                path.append((x, y))
        else: 
                y += 0
                x += 1
                path.append((x, y))
    return path 
                           
find_path(height)

path_line = find_path(height)
#print(find_path(height))

def plot_line_on_map():
    """this function takes a list of x, y coordinates from the find_path function and plots them on the map"""
    filename = 'five.png'
    image = Image.open(filename)
    # size = width
    # height = image.size
    for x in range(path_line):
        image.putpixel((x, y), (255, 0, 0, 255))
        image.save('path.png')

plot_line_on_map()
