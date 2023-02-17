import cv2
import numpy as np
import os

from tqdm import tqdm

# Define folder path
folder_path = "BDD/daytime_clear/VOC2007/JPEGImages/"

# Get list of image filenames in folder
image_filenames = os.listdir(folder_path)

# Initialize lists for mean and standard deviation values
means = []
stds = []

# Loop through images and calculate mean and standard deviation of pixel values
for filename in tqdm(image_filenames):
    # Load image
    img = cv2.imread(os.path.join(folder_path, filename))
    
    # Reshape image to a 2D array of pixels (rows, columns, channels) -> (pixels, channels)
    pixel_values = img.reshape(-1, img.shape[-1])
    
    # Calculate mean and standard deviation of pixel values for each channel
    channel_means = np.mean(pixel_values, axis=0)
    channel_stds = np.std(pixel_values, axis=0)
    
    # Append mean and standard deviation values to lists
    means.append(channel_means)
    stds.append(channel_stds)

# Calculate mean and standard deviation of mean and standard deviation values for each channel
mean_means = np.mean(means, axis=0)
mean_stds = np.mean(stds, axis=0)

print("Mean of means for each channel:", mean_means)
print("Mean of standard deviations for each channel:", mean_stds)