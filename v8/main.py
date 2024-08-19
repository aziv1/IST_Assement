import tensorflow as tf
import cv2
import numpy as np
import time
from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP, pause
import psutil
from picamera2 import Picamera2
from gpiozero import LED

# Load the Model
model = tf.keras.models.load_model("Model.h5")

# Preprocessing function for the image
def preprocess_image(image):
    resized_img = tf.image.resize(image, (150, 150))  # Resize image to match model's expected sizing
    normalized_img = resized_img / 255.0  # Normalize pixel values
    input_img = tf.expand_dims(normalized_img, axis=0)  # Add batch dimension
    return input_img

# Function to read image from webcam
def read_from_webcam():
    #Pi Camera Support
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()

    #LCD DEBUGGING
    lcd = LCD()

    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    
    #GPIO
    # 19 = 8, 16 = 4
    # 26 = 2, 20 = 1 
    gpio_pins = [LED(19), LED(16), LED(26), LED(20)]

    while True:
        # Non-Picamera Stuff
        frame = picam2.capture_array()   # Read a frame from the webcam
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # Preprocess the frame
        processed_frame = preprocess_image(frame)
        
        # Perform inference
        detect(processed_frame, model, lcd, gpio_pins)

def safe_exit(signum, frame):
    exit(1)

def get_cpu_temperature():
    temperature = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return temperature

# Function to perform detection
def detect(image, model, lcd, gpio_pins):
    start = time.time()
    # Perform inference
    predictions = model.predict(image)

    print(predictions)

    detected_class_index = np.argmax(predictions)
    class_names = ["Apple", "Banana", "Carambola", "Guava", "Kiwi", "Mango", "Orange", "Peach", "Pear", "Persimmon", "Pitaya", "Plum", "Pomegranate", "Tomatoes", "Muskmelon"]
    detected_class = class_names[detected_class_index]

    confidence = str(predictions)
    confidence = confidence.replace("[[", "")
    confidence = confidence.replace("]]", "")
    confidence = confidence.split(" ")
    detected = confidence.max()

    print(detected)

    print(f"Detected: {detected_class}")

    #LCD DEBUGGING
    end = time.time()
    cpu_temperature = get_cpu_temperature()
    lcd.text(f"FPS: {round((1000 * (end - start)), 2)} {round(cpu_temperature, 1)}C", 1)
    lcd.text(f"Seen: {class_names[detected_class_index]}", 2)

    encode(detected_class_index, gpio_pins)

def encode(detected_class_index, gpio_pins):
    if detected_class_index < 0 or detected_class_index > 15:
        raise ValueError("Input is out of range 1 -> 15")
    
    binary_string = format(detected_class_index, '04b') #Convert to 4bit binary string

    for i, bit in enumerate(binary_string):
        if bit == '1':
            gpio_pins[i].on()
            print(f"Set {gpio_pins[i]} to 1")
        else:
            gpio_pins[i].off()
            print(f"Set {gpio_pins[i]} to 0")

# Call the function to read from webcam
read_from_webcam()