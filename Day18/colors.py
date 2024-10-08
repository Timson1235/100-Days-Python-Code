import colorgram

# Absolute path to the image file
image_path = r"C:\Users\TimPr\100-Days-Python-Code-2\Day18\images.jpg"

rgb_colors = []
# Extract colors from the image
colors = colorgram.extract(image_path, 30)

# Convert the colors to RGB tuples
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)

color_rgbs = [(209, 147, 118), (148, 180, 157), 
 (228, 200, 113), (18, 12, 9), (33, 29, 31), (136, 92, 66),
   (92, 83, 87), (172, 112, 137), (222, 182, 172), (2, 9, 19), 
   (84, 97, 87), (139, 138, 139), (34, 41, 37), (186, 101, 83),
     (163, 143, 84), (116, 139, 122), (77, 56, 64),
       (73, 65, 44), (107, 47, 28), (60, 64, 73)]