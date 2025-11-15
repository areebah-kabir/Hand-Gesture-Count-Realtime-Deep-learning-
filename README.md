# HandCount - Real-Time Hand Gesture Detection and Finger Counter

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange?logo=google&logoColor=white)](https://mediapipe.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

HandCount is an open-source computer vision project that uses MediaPipe and OpenCV for real-time hand gesture detection. It processes video input from a webcam to identify hand landmarks and count raised fingers accurately. This project is suitable for gesture-based interfaces, interactive applications, or educational tools.

## Key Features

- Real-time hand tracking with MediaPipe's hand landmark model.
- Finger counting based on fingertip positions relative to joints.
- Video processing and visualization using OpenCV.
- Extensible design for additional gestures or multi-hand support.

## Tech Stack

| Tool       | Purpose                  | Version |
|------------|--------------------------|---------|
| Python    | Core scripting           | 3.7+   |
| MediaPipe | Hand detection           | 0.10+  |
| OpenCV    | Video capture and rendering | 4.5+ |
| NumPy     | Coordinate calculations  | 1.21+ |

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/TahaMazhar01/HandCount.git
   cd HandCount
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure a webcam or video source is available.

## Usage

1. Run the main script:
   ```
   python handcount.py
   ```

2. Position your hand in view of the camera; the finger count will display on the video feed.

3. Exit by pressing `q` or closing the window.

To use a video file instead of a webcam, modify the capture line in `handcount.py`:
```python
cap = cv2.VideoCapture('path/to/video.mp4')
```

## How It Works

1. Capture frames from the video source using OpenCV.
2. Detect hand landmarks with MediaPipe, extracting 21 key points (fingertips and joints).
3. Apply counting logic: Compare y-coordinates of fingertips to base joints; if the tip is higher, the finger is raised.
4. Render landmarks, connections, and the count overlay on the frame.

Example counting function from `handcount.py`:
```python
def count_fingers(landmarks):
    count = 0
    # Thumb
    if landmarks[4].y < landmarks[3].y:
        count += 1
    # Other fingers (index to pinky)
    finger_tips = [8, 12, 16, 20]
    for tip_id in finger_tips:
        if landmarks[tip_id].y < landmarks[tip_id - 2].y:
            count += 1
    return count
```

## Requirements

- Python 3.7–3.10
- Listed in `requirements.txt`:
  ```
  mediapipe>=0.10.0
  opencv-python>=4.5.0
  numpy>=1.21.0
  ```

## Roadmap

- Add multi-hand detection.
- Support additional gestures, such as thumbs up or victory sign.
- Optimize for mobile devices.
- Integrate web-based demos.

Suggestions can be submitted via issues.

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Description of changes"`.
4. Push the branch: `git push origin feature-name`.
5. Open a pull request.

Follow PEP 8 style guidelines. Include tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
Author: Areeba Kabir
GitHub: AreebaKabir
Email: areebakabir196@gmail.com

For questions or feedback, open an issue or email the author.
