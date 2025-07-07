
# Paddy Disease Classification 🌾🔬

A deep learning-based web application for classifying paddy (rice plant) diseases using transfer learning with DenseNet201 and Django as the web interface.

---

## 📌 Overview

This project implements a **Convolutional Neural Network (CNN)** model using **DenseNet201** via transfer learning to classify paddy leaf diseases into three categories. It includes a full-stack interface built with **Django**, making it accessible and user-friendly.

---

## 🧠 Deep Learning Background

**Deep Learning (DL)** is a subfield of Machine Learning that mimics the human brain to process complex data. DL is especially powerful in handling unstructured data such as images and audio. Common DL architectures include:

- **Convolutional Neural Networks (CNN)**
- **Multilayer Perceptrons (MLP)**
- **Recurrent Neural Networks (RNN)**

---

## 🌀 CNN and DenseNet201

**Convolutional Neural Network (CNN)** is a neural network architecture that is widely used for image classification, object detection, and segmentation. In this project, we use **DenseNet201**, a powerful CNN variant that:

- Connects each layer to every other layer (feed-forward)
- Reduces vanishing gradient problems
- Improves feature propagation
- Reuses features efficiently
- Reduces the number of parameters

---

## 🏷️ Features

- Classification of paddy diseases into **three categories**
- Trained using **transfer learning** with DenseNet201
- Web interface built with **Django**
- Upload image and get prediction in real-time

---

## 🗂️ Dataset & Source Code

All dataset and source code for training, model deployment, and web interface are included in this repository.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/paddy-desease.git
cd paddy-desease/web/paddy
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Upgrade pip and Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Django (if not already installed)

```bash
pip install django
python -m django --version
```

### 5. Run Django Server

```bash
python manage.py runserver
```

---

## 📝 Tech Stack

- **Python 3.10+**
- **TensorFlow 2.11.0**
- **Keras 2.11.0**
- **Django**
- **DenseNet201 (Transfer Learning)**

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`:

```
keras==2.11.0
numpy==1.23.5
Pillow==9.3.0
tensorflow==2.11.0
tensorflow_intel==2.11.0
```

---

## 📸 Preview

_Screenshots or demo GIF can be added here_

---

## 📬 Contact

For any questions or collaborations, feel free to reach out:
- ✉️ Email: your@email.com
- 📂 GitHub: [your-username](https://github.com/your-username)

---

## ✅ License

This project is licensed under the MIT License.
