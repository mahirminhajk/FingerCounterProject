# FingerCounterProject

FingerCounterProject is a Python application that uses MediaPipe and OpenCV to track fingers in real-time. This project detects hand landmarks and calculates the position of fingers, displaying the live feed along with finger coordinates and frames per second (FPS).

## Features

- Real-time hand and finger tracking using MediaPipe.
- Displays hand landmarks on the video feed.
- Outputs the position of specific landmarks.
- Shows the FPS of the video feed.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install Dependencies:**
   Make sure you have Python installed. Then, install the required packages using pip:
   ```bash
   pip install opencv-python mediapipe   
   ```

## Usage
1. **Run the Application:**
   ```bash
   python main.py
   ```
2. **Contorls:**
  - ESC: Close the application.

## Code Explanation
- handDetector Class:
  - Initializes MediaPipe Hands with specified parameters.
  - findHands: Detects hands in the image and draws landmarks if required.
  - findPosition: Finds and returns the position of landmarks for a specified hand.

- main Function:
  - Captures video from the default camera.
  - Processes each frame to detect hands and find landmark positions.
  - Displays the FPS on the video feed.

## Example

## Acknowledgements
pecial thanks to the MediaPipe and OpenCV libraries for their powerful tools for computer vision and image processing.

