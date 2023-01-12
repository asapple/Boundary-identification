img = ''
with open("output-hsv.txt", "r") as file:
    for line in file:
        lineStr = line.strip()
        v = lineStr.split()[-1]
        if float(v) > 35:
            img += '0'
        else:
            img += '1'
overview = ''
accumulator = 0
for i in range(len(img)-1):
    accumulator += 1
    if img[i]!=img[i+1] or i == len(img) - 2:
        overview += img[i] + ' ' + str(accumulator) + '\n'
        accumulator = 0
with open("output-line.txt", "w") as file:
    file.write(overview + '\n')
    file.write(img)
