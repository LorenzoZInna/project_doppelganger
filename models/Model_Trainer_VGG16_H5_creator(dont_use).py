import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import Adam

# Define paths to the datasets
happy_dir = '../raw_data/Happy_Sad/data/happy'
sad_dir = '../raw_data/Happy_Sad/data/sad'

# Define constants
IMAGE_SIZE = (150, 150)
BATCH_SIZE = 32

# Define data generators
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    preprocessing_function=preprocess_input  # Preprocess input according to VGG16 requirements
)

train_generator = train_datagen.flow_from_directory(
    directory='../raw_data/Happy_Sad/data',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=True
)

# Load the VGG16 model without the top (fully connected) layers
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))

# Freeze the base model layers
base_model.trainable = False

# Create a new model on top of the base model
model = Sequential([
    base_model,
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=10)

# Save the model as an H5 file
model.save('happy_sad_vgg16_model.h5')
