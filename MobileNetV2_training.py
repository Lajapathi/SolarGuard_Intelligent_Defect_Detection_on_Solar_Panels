import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

dir_path = "/Users/apple/Documents/Guvi/Projects/Solar gaurd /Intelligent Defect Detection on Solar Panels/Faulty_solar_panel"

# Data generator with preprocessing matching MobileNetV2
datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2,
    horizontal_flip=True,
    rotation_range=20,
    zoom_range=0.2
)

train_images = datagen.flow_from_directory(
    dir_path,
    target_size=(500,500),  # MobileNetV2 expects 224x224 inputs
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

test_images = datagen.flow_from_directory(
    dir_path,
    target_size=(500,500),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Load MobileNetV2 without top classifier layers, with pretrained weights
base_model = MobileNetV2(input_shape=(500,500,3), include_top=False, weights='imagenet')

# Freeze the convolutional base so initial training doesn't change it
base_model.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dense(6, activation='softmax')  # 6 classes in your dataset
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, validation_data=test_images, epochs=18)

model.save('solardetection_model_500_E18.h5')
print("solardetection_model_500_E185")