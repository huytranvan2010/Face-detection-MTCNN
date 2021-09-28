import cv2
import mtcnn 

# face detection
img = cv2.imread('image_3.jpg')
# chuyển từ BGR -> RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detector = mtcnn.MTCNN()   # đang để mọi thứ mặc định
faces = detector.detect_faces(img_rgb)

# kiểm tra định dạng của kết quả
# print(type(faces))
# print(faces)

# vẽ keypoints và bounding boxes
def draw(image, face):
    x, y, width, height = face['box']
    cv2.rectangle(image, (x, y), (x+width, y+height), (0, 155, 255), 2)

    for key, value in face['keypoints'].items():
        cv2.circle(image, value, 2, (0, 155, 255), 2)

# tạo ảnh mới với id khác
img_copy = img.copy()   

for face in faces:
    draw(img_copy, face)

# Hiển thị ảnh
cv2.imshow("Image", img_copy)
# Lưu lại ảnh
cv2.imwrite('new_image.jpg', img_copy)
cv2.waitKey(0)

""" Trích xuất các ảnh ra, trích xuất xong có thể lưu vào các file"""
def draw_faces(face):
    x, y, width, height = face['box']
    data = img[y:y+height, x:x+width]
    cv2.imshow("face", data)
    cv2.waitKey(0)

for face in faces:
    draw_faces(face)
