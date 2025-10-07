import cv2

# Load the image

image = cv2.imread(r'D:\cv open\p1.jpg')
#covnvert image to gray_scale
gray_image=cv2.cvt.Color(image,cv2.COLOR_BGR2GRAY)

# Create a resizable window

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

# Resize the same window

cv2.resizeWindow('gray_image', (224, 224))

# Display the image

cv2.imshow('Processed_Image', resized_image)

key=cv2.waitKey(0)

#check if the S key was pressed (ASCI||for 'S' is 83)
if key==ord('s'):
    #save the processed image when s is pressed
    cv2.imwrite("grayscale_resized_image.jpg")
    print("Image saved as gray_scale_resized_image.jpg")
else:
    print("Image not saved")

cv2.destroyAllWindows()

# Print image properties

print(f"Image Dimensions: {image.shape}") # height, width, channels
