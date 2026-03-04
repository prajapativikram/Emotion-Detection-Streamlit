# 🎭 Emotion Detection Web App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success)

A deep learning-powered web application that detects human emotions from facial images using a Convolutional Neural Network (CNN). Users can upload images to get emotion predictions instantly through a clean web interface built with Streamlit.

---

## 🚀 Live Demo

🎉 **Live App:** [https://prajapativikram-emotion-detection-streamlit.streamlit.app](https://emotion-detection-app-2309.streamlit.app/)  
📂 **GitHub Repo:** https://github.com/prajapativikram/Emotion-Detection-Streamlit

---

## 🔍 About the Project

This project demonstrates how deep learning can be applied to real-world visual emotion recognition. It uses a trained CNN model to classify face images into seven emotions:

- Angry      
- Happy  
- Sad  
- Surprised  
- Neutral

The interface lets users upload a photo, and the app returns the predicted emotion with minimal latency.

---

## 🧠 Model Details

- **Model Type:** Convolutional Neural Network (CNN)  
- **Input:** 48×48 grayscale image  
- **Classes:** 7 distinct emotional categories  
- **Preprocessing:**  
  - Grayscale conversion  
  - Normalization  
  - Resizing to 48×48 pixels

> 💡 *Achieved 72% validation accuracy on test dataset.*  

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Deep Learning | TensorFlow |
| Image Processing | OpenCV |
| UI/Web App | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```text
Emotion-Detection-Streamlit/
│
├── main.py
├── emotion_detection_model.h5
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation (Run Locally)

**1️⃣ Clone the Repository**

```bash
git clone https://github.com/prajapativikram/Emotion-Detection-Streamlit.git
cd Emotion-Detection-Streamlit
```

**2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

**3️⃣ Run the Application**

```bash
python -m streamlit run main.py
```


---

## 📸 How It Works

1. User uploads an image.
2. Image is converted to grayscale.
3. Image resized to 48x48.
4. Pixel values normalized.
5. CNN model predicts emotion.
6. Result displayed on web interface.

---

## 👨‍💻 Author

Vikram Kumar  
Bachelor of Technology – Computer Science  
Aspiring AI/ML Engineer

---

## ⭐ If You Like This Project

Give this repository a star on GitHub!
