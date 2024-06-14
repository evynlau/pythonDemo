from PIL import Image
import cv2
import numpy as np

# Load the image
input_path = "C:\Users\RS8636\Pictures\1000030259.jpg"
image = Image.open(input_path)


# Convert the image to a format OpenCV can work with
image = np.array(image)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray_image = cv2.medianBlur(gray_image, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(
    gray_image, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blockSize=9,
    C=2
)

# Convert back to color, so the edges are in the alpha channel
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Reduce the color palette of the image
num_colors = 25  # Number of colors to reduce the image to
data = np.float32(image).reshape((-1, 3))

# Define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
K = num_colors
_, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert back to 8 bit values
center = np.uint8(center)
result = center[label.flatten()]
result = result.reshape(image.shape)

# Combine the color-reduced image with the edges
cartoon_image = cv2.bitwise_and(result, edges_colored)

# Save the result
output_path = "/mnt/data/cartoon_image.png"
cv2.imwrite(output_path, cartoon_image)

output_path
