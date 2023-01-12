from PIL import Image
img = Image.open("images/test.jpg")
img = img.convert("HSV")
pixels = img.load()
linesAverageHSV = []
width, height = img.size
for y in range(height):
    r, g, b = 0, 0, 0
    for x in range(int(width/4)):
        r += pixels[x, y][0]
        g += pixels[x, y][1]
        b += pixels[x, y][2]
    r_avg = r/width
    g_avg = g/width
    b_avg = b/width
    linesAverageHSV.append((r_avg, g_avg, b_avg))

with open("output-hsv.txt", "w") as output_file:
    for i, line_average_rgb in enumerate(linesAverageHSV):
        output_file.write("Line {}: Average HSV: {} {} {}\n".format(i, int(line_average_rgb[0]), int(line_average_rgb[1]), int(line_average_rgb[2])))