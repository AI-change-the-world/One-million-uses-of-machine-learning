import cv2

high_dpi_image_path = "D:\\github_repo\\One-million-uses-of-neural-networks\\images\\0_high_dpi.jpg"
img = cv2.imread(high_dpi_image_path)
img = cv2.resize(img,(256,256))
img = cv2.resize(img,(1024,1024))
cv2.imwrite("D:\\github_repo\\One-million-uses-of-neural-networks\\images\\0_low_dpi.jpg",img)