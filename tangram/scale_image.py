from PIL import Image
import math
# Open an image file
with Image.open('tangram\Children.png') as img:
    # Original size
    orig_width, orig_height = img.size

    # Define the desired width or height and calculate the other dimension to maintain aspect ratio
    #scale_factor = 0.55
    
    # Calculate the new dimensions
    new_width = int(800)
    new_height = int(800)

    # Resize the image
    resized_img = img.resize((new_width, new_height))

    # Save the scaled image
    resized_img.save('tangram\Children_new.png')