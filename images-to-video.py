import cv2
import os
import re
from tkinter import Tk
from tkinter import filedialog, simpledialog, messagebox

def create_video(image_folder, output_video_file, fps=30):
    # Get a list of all images in the folder and the file extension
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort() 

    # Get the dimensions from the first image
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Set up for mp4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    # Loop through all images and add them to the video
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        # Add each frame to the video
        video.write(frame)

    video.release()

    # Show popup message for success
    Tk().withdraw() 
    messagebox.showinfo("Success", f"Video created successfully and saved as {output_video_file}")

def extract_base_name(image_filename):
    # Use regular expression to strip the numerical part from the image sequence name
    base_name = re.sub(r'\d+$', '', os.path.splitext(image_filename)[0])
    return base_name

def get_image_folder_and_output():
    # open a file dialog to select the first image
    Tk().withdraw() 
    first_image_path = filedialog.askopenfilename(title="Select the first image in the sequence", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    if not first_image_path:
        print("No image selected. Exiting.")
        return None, None, None

    # Extract the folder path and base name from the selected file
    image_folder = os.path.dirname(first_image_path)
    image_filename = os.path.basename(first_image_path)
    base_name = extract_base_name(image_filename)

    fps = simpledialog.askinteger("Input", "Enter the frame rate (FPS):", minvalue=1, maxvalue=60)

    if not fps:
        print("No frame rate entered. Exiting.")
        return None, None, None

    # the output video file name (same folder as image sequence)
    output_video_file = os.path.join(image_folder, f"{base_name}_final.mp4")

    return image_folder, output_video_file, fps

# Main script execution
if __name__ == "__main__":
    image_folder, output_video_file, fps = get_image_folder_and_output()
    
    if image_folder and output_video_file and fps:
        create_video(image_folder, output_video_file, fps)
