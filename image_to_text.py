from PIL import Image
import statistics

image = Image.open("image_to_text/Screenshot 2025-03-09 180607.png")
ascii_grayscale = list("@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'.  ")

text_image = ""
previous_line = []
current_line = []
ascii_line = []
flip_flop = 1

resize = image.size[0] // 2, image.size[1] // 2
print(resize)
new_image = image.resize(resize)

px = new_image.load()

for y in range(1, resize[1]): # iterate through the rows
    previous_line = current_line
    current_line = []
    ascii_line = []
    for x in range(1, resize[0]): # determines ascii char for every pixel in row (iterates through colummns)
        pixel = px[x, y]

        #convert the rgb value of the pixel to a grayscale, then normalize to a range of 70 for the ascii chars
        grayscale = ((0.2989 * pixel[0] + 0.5870 * pixel[1] + 0.1140 * pixel[2])/255)*70
        current_line.append(int(grayscale))

        print(f"Grayscale: {grayscale}, RGB: {pixel}, ASCII: {ascii_grayscale[int(grayscale)]}")
    
    #on the second row and onward, compare the current and previous row and turn them into one averaged row
    if flip_flop == 1:    
        if y > 1:
            for i in range(1, resize[0]-1):
                ascii_line.append(statistics.mean([current_line[i], previous_line[i]]))

        for i in ascii_line:
            text_image = text_image + ascii_grayscale[int(i)]
        text_image = text_image + "\n"
        flip_flop = 0
    else:
        flip_flop = 1
        
lines_count = text_image.count('\n') + 1
print(lines_count)
print(text_image)
