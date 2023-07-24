from PIL import Image

# Rasmni ochish
img = Image.open('image5.jpg')
# Rasmni 90 gradusga aylantirish
img = img.rotate(90)

# Rasmni o'lchamlarini olish
width, height = img.size

# Rasmni o'lchamini kichraytirish
new_width = 100
new_height = int(new_width * height / width)
img = img.resize((new_width, new_height))
	
# Rasmni har bir pikselini tekshirish
for y in range(new_height):
    for x in range(new_width):
        # Piksel rangini olish
        r, g, b = img.getpixel((x, y))
        # ANSI kod yordamida matn rangini o'zgartirish
        print(f'\033[38;2;{r};{g};{b}m█', end='')
    # Yangi qatorga o'tish
    print()
