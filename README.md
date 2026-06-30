# 📖 OpenCV Hand Tracking & Gesture Control

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge\&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge\&logo=numpy)

A real-time computer vision project built with **Python**, **OpenCV**, and **MediaPipe** for detecting hand landmarks and controlling applications using hand gestures. The project includes gesture-based system volume control, real-time finger counting, and a reusable hand tracking module that can be integrated into other computer vision applications.

---

# 📌 Project Overview

This project demonstrates how computer vision and hand tracking can be used to create touch-free interactions with a computer. Using a webcam, the application detects hand landmarks in real time and processes them to recognize different gestures.

The project includes multiple applications such as controlling the system volume by measuring the distance between the thumb and index finger, counting raised fingers, and a reusable hand tracking module for future gesture-based projects.

It is built using **OpenCV** for video processing, **MediaPipe** for accurate hand landmark detection, and **NumPy** for mathematical calculations.

---

# ✨ Features

### ✋ Hand Tracking

* Real-time hand detection
* Detects 21 hand landmarks
* Supports multiple hand gestures

---

### 🔊 Volume Control

* Control system volume using hand gestures
* Measures thumb and index finger distance
* Smooth real-time volume adjustment

---

### ✋ Finger Counter

* Detects raised fingers
* Displays live finger count
* Works in real time using webcam input

---

### 🛠️ Reusable Hand Tracking Module

* Object-oriented hand tracking class
* Easy integration into other OpenCV projects
* Simplifies landmark detection and coordinate extraction

---

# 🛠️ Technologies Used

* Python 3
* OpenCV
* MediaPipe
* NumPy

---

# 📂 Project Structure

```text
OpenCV-Hand-Tracking/
│
├── FingerImages/
│
├── HandTrackingModule.py
├── HandTrckingMin.py
├── opencvSETUP.py
├── Proj1VolumeHandControl.py
├── Proj2FingerCounter.py
├── fyp_proto_handgesture.py
├── myNewGameHandTrack.py
├── test.py
│
├── .gitignore
└── README.md
```

---

# ⚙️ Applications

## 🔊 Gesture Volume Controller

* Detects thumb and index finger
* Calculates distance between fingers
* Maps the distance to the system volume level

---

## ✋ Finger Counter

* Detects hand landmarks
* Counts the number of raised fingers
* Displays the finger count in real time

---

## 🛠️ Hand Tracking Module

A reusable Python module that provides:

* Hand detection
* Landmark extraction
* Finger position detection
* Easy integration with other projects

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/your-username/OpenCV-Hand-Tracking.git
```

---

## Navigate to Project

```bash
cd OpenCV-Hand-Tracking
```

---

## Install Dependencies

```bash
pip install opencv-python mediapipe numpy
```

---

## Run Volume Control

```bash
python Proj1VolumeHandControl.py
```

---

## Run Finger Counter

```bash
python Proj2FingerCounter.py
```

---

# 📂 Main Files

| File                        | Description                             |
| --------------------------- | --------------------------------------- |
| `HandTrackingModule.py`     | Reusable hand tracking module           |
| `Proj1VolumeHandControl.py` | Gesture-based volume controller         |
| `Proj2FingerCounter.py`     | Real-time finger counting               |
| `HandTrckingMin.py`         | Basic hand tracking example             |
| `opencvSETUP.py`            | Webcam setup and testing                |
| `fyp_proto_handgesture.py`  | Prototype for gesture-based interaction |
| `myNewGameHandTrack.py`     | Hand tracking for game control          |

```

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

* Computer Vision
* Real-Time Image Processing
* Hand Landmark Detection
* Gesture Recognition
* OpenCV
* MediaPipe
* Python Programming
* Mathematical Coordinate Calculations
* Human-Computer Interaction (HCI)

---

# 👩‍💻 Author

**Rameesha Shahid**

Software Engineering Student

**Areas of Interest**

* Artificial Intelligence
* Computer Vision
* Machine Learning
* Full-Stack Development
* Mobile Application Development

---

# 📄 License

This project is developed for learning and educational purposes.
