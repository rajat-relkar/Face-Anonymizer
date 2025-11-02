# 🕵️‍♂️ Face Anonymizer

**Face Anonymizer** is a simple yet powerful Python tool that automatically detects faces in images, videos, or webcam streams and anonymizes them by applying blur.  
It uses **MediaPipe Face Detection** for accurate and fast face localization and **OpenCV** for blurring.

---

## Features

- Detects faces using **MediaPipe**
- Supports **image**, **video**, and **webcam** modes
- Blurs faces to ensure privacy
- Automatically saves processed outputs
- Minimal setup, no deep learning model training required

---

## Tech Stack

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://developers.google.com/mediapipe)
- Python 3.8+

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/face-anonymizer.git
cd face-anonymizer
pip install -r requirements.txt
```

**`requirements.txt`**
```
opencv-python
mediapipe
```

---

## Usage

Run the script in one of three modes: **image**, **video**, or **webcam**.

### 1. Image Mode
```bash
python face_anonymizer.py --mode image
```
- Expects image in `./data/myimg.png`
- Output saved to `./data/output/output.png`

### 2. Video Mode
```bash
python face_anonymizer.py --mode video --filePath ./data/testvideo1.mp4
```
- Processes the input video
- Saves output video to `./data/output/output.mp4`

### 3. Webcam Mode
```bash
python face_anonymizer.py --mode webcam
```
- Opens webcam and anonymizes faces in real-time
- Press `Ctrl + C` or close the window to stop

---

## 📂 Project Structure

```
face-anonymizer/
│
├── face_anonymizer.py       # Main script
├── data/
│   ├── myimg.png            # Example input image
│   ├── testvideo1.mp4       # Example input video
│   └── output/              # Output folder (auto-created)
│
├── requirements.txt
└── README.md
```

---

## How It Works

1. **Face Detection:** Uses MediaPipe’s pre-trained `FaceDetection` model.  
2. **Bounding Box Extraction:** Converts normalized coordinates to pixel values.  
3. **Anonymization:** Applies Gaussian blur to the detected face region using OpenCV.  
4. **Output:** Saves the processed image/video or displays live webcam feed.

---


## Notes

- The **`model_selection`** parameter can be set to:
  - `0` → Best for faces within 2 meters.
  - `1` → Best for faces within 5 meters.
- Adjust the blur strength via `k_size` in the code (default = 50).

---
