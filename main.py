import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# Load model
model = load_model("emotion_detection_model.h5")

# Emotion labels (change if your order is different)
emotion_labels = ['Angry', 'Happy', 'Sad', 'Surprised', 'Neutral']

st.title("Human Emotion Detection")

st.write("Upload a face image and the model will predict the emotion.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize to model input size (48x48)
    resized = cv2.resize(gray, (48, 48))
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 48, 48, 1))

    # Prediction
    prediction = model.predict(reshaped)
    emotion_index = np.argmax(prediction)
    emotion = emotion_labels[emotion_index]

    st.success(f"Predicted Emotion: {emotion}")