import tensorflow as tf
import cv2
import numpy as np

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
    cap = cv2.VideoCapture(0)  # Open the webcam (change the number based on your camera setup)
    while True:
        ret, frame = cap.read()  # Read a frame from the webcam
        if not ret:
            print("Failed to grab frame")
            break
        
        # Preprocess the frame
        processed_frame = preprocess_image(frame)
        
        # Perform inference
        detect(processed_frame, model)
        
        # Break the loop if 'q' is pressed
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
    
    cap.release()
    cv2.destroyAllWindows()

# Function to perform detection
def detect(image, model):
    # Perform inference
    predictions = model.predict(image)

    print(predictions)
    
    detected_class_index = np.argmax(predictions)
    class_names = ["Apple", "Banana", "3", "4", "5", "Lemon", "Orange", "8", "9", "10", "11", "12", "13", "14", "15"]
    detected_class = class_names[detected_class_index]

    print(f"Detected: {detected_class}")

# Call the function to read from webcam
read_from_webcam()
