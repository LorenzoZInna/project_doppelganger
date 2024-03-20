from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

def image_preprocessing(inputImage):

     # Preprocess the image
    image= Image.open(inputImage)
    target_size = (150, 150)  # Adjust according to your model's input size
    image = image.resize(target_size)
    image_array = np.array(image)
    image_array = image_array.astype('float32') / 255.0  # Normalize pixel values
    return image_array
