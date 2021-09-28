import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()
video = cv2.VideoCapture(0)     # dùng webcam, nếu có video thì truyền đường dẫn vào

while True:
    # lấy frame
    ret, frame = video.read()

    faces = detector.detect_faces(frame)
    
    if faces != []:
        # duyệt qua các face phát hiện được
        for face in faces:
            x, y, width, height = face['box']
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 155, 255), 2)

        for key, value in face['keypoints'].items():
            cv2.circle(frame, value, 2, (0, 155, 255), 2)

    # hiển thị kết quả
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # nhấn q nếu muốn thoát
        break

video.release()
cv2.destroyAllWindows()