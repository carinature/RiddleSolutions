import PIL.Image

# ascii charachters used to build the output text
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']  # , ' ']
# ASCII_CHARS = ['@', '#', '$', '%', '?', '*', '^', '~', '-',  '.' , ' ']
# ASCII_CHARS = [ 'g', 'e', 'o', 'r', 'g', 'e', '+' , '-' , '.' ,' '] #,  '*', '+', ';', '-',  '.' , ' ']
# ASCII_CHARS = list('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.')
# ASCII_CHARS = list("@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-`")
print(f'chars {len(ASCII_CHARS)}')



# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    # ratio = height / width
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert('L')  # pass 'L' to convert to grayscale
    return grayscale_image


# convert pixels to a string of ASCII chars
def pixels_to_acsii(image):
    pixels = image.getdata()
    # for pixel in pixels:
    #     pixel
    print(list(pixels))
    chars = ''.join([ASCII_CHARS[pixel // (1 + 255//len(ASCII_CHARS))] for pixel in pixels])
    # chars = ''.join([ASCII_CHARS[pixel // 4] for pixel in pixels])

    return chars


def main(new_width=100):
    # attemp to open image from user-input
    # path = input("Enter a valid pathname to the image:\n")
    # print(f'path - {path}')
    # print(f'path - {path.encode()}')
    path = None
    if not path:
        path = '/home/ge/Pictures/ge.jpeg'
        # path = '/home/ge/PycharmProjects/RiddleSolutions/MiniProjects/Scrapers/babYoda22.jpg'

    try:
        image = PIL.Image.open(path)
        new_width, _ = image.size

        # convert image to ascii
        new_image_data = pixels_to_acsii(grayify(resize_image(image, new_width)))

        # format
        pixel_count = len(new_image_data)
        ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        # print(ascii_image)
        import time
        # from datetime import time
        with open('asciiimage'+time.ctime()+'.txt', 'w') as f:
            f.write(ascii_image)
    except:
        print(path, 'is not a valid pathname to an image')


if __name__ == '__main__':
    main()
