import cv2

# -------------------------------------
# Step 1: Load the image
# -------------------------------------
image = cv2.imread(r'D:\cv open\p1.jpg')

# Check if image is loaded properly
if image is None:
    print("❌ Error: Could not read the image. Please check the file path.")
    exit()

# -------------------------------------
# Step 2: Convert the image to grayscale
# -------------------------------------
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -------------------------------------
# Step 3: Resize the grayscale image to 224x224
# -------------------------------------
resized_image = cv2.resize(gray_image, (224, 224))

# -------------------------------------
# Step 4: Display the processed image
# -------------------------------------
cv2.imshow('Processed_Image', resized_image)

# Wait for a key press
key = cv2.waitKey(0)

# -------------------------------------
# Step 5: Check if 'S' key was pressed to save the image
# -------------------------------------
if key == ord('s') or key == ord('S'):
    cv2.imwrite("grayscale_resized_image.jpg", resized_image)
    print("✅ Image saved as grayscale_resized_image.jpg")
else:
    print("❌ Image not saved")

# -------------------------------------
# Step 6: Close all OpenCV windows
# -------------------------------------
cv2.destroyAllWindows()

# -------------------------------------
# Step 7: Print image properties
# -------------------------------------
print(f"📏 Original Image Dimensions: {image.shape}")  # (height, width, channels)
