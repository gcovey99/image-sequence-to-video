# Image Sequence to Video Creator

This allows users to create a video from a sequence of images stored in a specified folder. It uses the OpenCV library for video creation and Tkinter for graphical user interaction, such as selecting the image folder and providing the frame rate (FPS) for the video. This is mainly for animation that is rendered in an series of images. Based on your render engine it could take longer to render in video format, or the video format quality is not as good as an image sequence.

## Features

- Select images from a folder and compile them into a video.
- Supports `.png`, `.jpg`, and `.jpeg` image formats.
- Allows users to specify the frame rate (FPS) for the video.
- Automatically sorts images to maintain sequence order.
- Saves the video in MP4 format mp4.
 
## Requirements

- OpenCV (`cv2`)
- Tkinter (usually included with Python)
- OS module
- re module

