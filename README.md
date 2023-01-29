# Face-Landmarks-Detection-in-Real-Time

This repository contains a Python script that uses MediaPipe to detect 468 face landmarks in real-time and on images.

# Requirements
 - Python 3.9.1
 - MediaPipe
 - OpenCV
 
# Installation
1. Clone the repository to your local machine
```bash
git clone https://github.com/VivekSai07/Face-Landmarks-Detection-in-Real-Time.git
```

2. Install the required packages
```bash
pip install opencv-python
```

3. Install MediaPipe
```bash
pip install --upgrade --user pip
pip install --upgrade --user setuptools
pip install --user mediapipe

```

# Additional Information
- This script uses the [MediaPipe Facemesh](https://google.github.io/mediapipe/solutions/face_mesh.html#:~:text=MediaPipe%20Face%20Mesh%20is%20a,for%20a%20dedicated%20depth%20sensor.) model to detect face landmarks.
- The script is compatible with both JPEG and PNG images.

# Contributions
I welcome any contributions to this project. If you would like to make a change, please fork the repository, make your changes and create a pull request.

# Acknowledgements
MediaPipe for providing the Facemesh model
OpenCV for providing image processing capabilities.
