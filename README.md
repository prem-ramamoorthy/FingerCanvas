# FingerCanvas 

FingerCanvas is a computer vision-based virtual drawing application that allows users to draw on the screen using hand gestures — no mouse or touchscreen needed! Built with Python, OpenCV, and a hand detection module (MediaPipe or custom), this project tracks your finger movements to draw, erase, change brush colors, and even adjust brush thickness dynamically.

---

## Features

- Draw using your index finger
- Two fingers to enter color/eraser selection mode
- Erase with the black color tool
- Pinch to adjust brush thickness
- Overlays for logo, color palette, and banner
- Flipped camera view for natural UX
- Save your canvas with a keypress (`s`)
- Clear canvas with five-finger gesture

---

## Tech Stack

- **Python**
- **OpenCV**
- **NumPy**
- **Custom `handDetection.py`** (uses [MediaPipe](https://google.github.io/mediapipe/) or a custom solution)

---

## Project Structure
```bash
FingerCanvas/
├── images/
│ ├── banner.jpg
│ ├── colors.jpg
│ ├── eraser.jpg
│ └── logo.jpg
├── handDetection.py
├── fingerCanvas.py # main script
└── README.md
```

---
## 🎮 Controls

| Gesture                | Action                    |
|------------------------|---------------------------|
| ☝️ One Finger (Index)  | Draw on the canvas        |
| ✌️ Two Fingers (Index + Middle) | Select color or eraser from top bar |
| 🤏 Thumb + Index        | Adjust brush thickness    |
| 🖐️ All Five Fingers    | Clear the entire canvas   |
| `s` key                | Save current drawing as PNG |
| `d` key                | Exit the application      |

