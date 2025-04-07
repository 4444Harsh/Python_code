from PIL import Image # pip install pillow 
import numpy as np # pip install numpy 

def image_to_array(image_path): 
    # Open an image file 
    with Image.open(image_path) as img: 
    # Convert image to numpy array 
    img_array = np.array(img) 
    return img_array 
# Example usage 
image_path = 'my_image.jpg' 
# image path 
img_array = image_to_array(image_path) 
print(img_array)
