from PIL import Image

# Open the image file
img = Image.open('C:/Users/ENeS/OneDrive - 室蘭工業大学/デスクトップ/tangram/golden_para.png').convert('RGBA')
width, height = img.size

# Prussian blue in RGBA (Prussian blue RGB is (0, 49, 83), 255 is for full opacity)
golden = (0, 0, 0, 255)

# Load the pixel data
data = img.load()

# Iterate over each pixel
for y in range(height):
    for x in range(width):
        # Get the RGBA value of the pixel
        r, g, b, a = data[x, y]
        
        # Define the condition to change the color - this assumes the triangle is not pure white or black
        # You may need to adjust the condition based on the color of the triangle
        if not (r > 250 and g > 250 and b > 250) and a > 0:  # not white and not fully transparent
            data[x, y] = golden

# Save the modified image

img.save('para_shadow.png')
print(img.size)