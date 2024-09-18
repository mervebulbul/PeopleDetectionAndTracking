import cv2
import time
from ultralytics import YOLO  

grid_size = 6 # 6x6 grid
grid_center = int(grid_size / 2)
grid_spacing = 60

# camera settings
camera_Width = 1024
camera_Heigth = 780

# color and thickness of grid lines
lineColor = (0, 255, 0)
lineThickness = 1

# color and thickness of messages
colorWhite = (255, 255, 255)
colorRed = (0, 0, 255)  
messageThickness = 2

# threshold for person detection
confidence_threshold = 0.5  

dsize = (camera_Width, camera_Heigth)

# draw grid lines
def displayGrid(frame):
    # 6x6 grid 
    for i in range(grid_size):
        cv2.line(frame, (int(camera_Width / grid_size) * i, 0), (int(camera_Width / grid_size) * i, camera_Heigth), lineColor, lineThickness)
        cv2.line(frame, (0, int(camera_Heigth / grid_size) * i), (camera_Width, int(camera_Heigth / grid_size) * i), lineColor, lineThickness)

    # Grid lines
    cv2.line(frame, (int(camera_Width / 2), 0), (int(camera_Width / 2), camera_Heigth), lineColor, lineThickness)
    cv2.line(frame, (0, int(camera_Heigth / 2)), (camera_Width, int(camera_Heigth / 2)), lineColor, lineThickness)


def calculatePositionForDetectedPerson(frame, x, y, h, w):
    cx = int(x + (w / 2))  # x center of person
    cy = int(y + (h / 2))  # y center of person
    dir_list = []

    if cx < int(camera_Width / 2) - grid_spacing * grid_center:
        if cx < int(camera_Width / 2) - 2 * grid_spacing * grid_center:
            dir_list.append("GO FAR LEFT")
        else:
            dir_list.append("GO LEFT")
    elif cx > int(camera_Width / 2) + grid_spacing * grid_center:
        if cx > int(camera_Width / 2) + 2 * grid_spacing * grid_center:
            dir_list.append("GO FAR RIGHT ")
        else:
            dir_list.append("GO RIGHT ")

    if cy < int(camera_Heigth / 2) - grid_spacing * grid_center:
        if cy < int(camera_Heigth / 2) - 2 * grid_spacing * grid_center:
            dir_list.append("GO FAR UP")
        else:
            dir_list.append("GO UP")
    elif cy > int(camera_Heigth / 2) + grid_spacing * grid_center:
        if cy > int(camera_Heigth / 2) + 2 * grid_spacing * grid_center:
            dir_list.append("GO FAR DOWN")
        else:
            dir_list.append("GO DOWN")

    if not dir_list:
        cv2.putText(frame, "CENTER", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, colorRed, 2)
    else:
        cv2.putText(frame, " ".join(dir_list), (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, colorRed, 2)

    cv2.line(frame, (int(camera_Width / 2), int(camera_Heigth / 2)), (cx, cy), colorWhite, messageThickness)
    cv2.rectangle(frame, (x, y), (x + w, y + h), colorRed, messageThickness)
    cv2.putText(frame, str(int(x)) + " " + str(int(y)), (x - 20, y - 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, colorRed, messageThickness)


# Upload YOLOv8 model 
model = YOLO('yolov8n.pt')  

video_capture = cv2.VideoCapture('/add/your/video/path.mp4')
time.sleep(1.0)

while True:
    ret, frameOrig = video_capture.read()
    if not ret:
        break

    frame = cv2.resize(frameOrig, dsize)
    displayGrid(frame)

    results = model(frame)  # Prediction with YOLOv8 

    for result in results:
        boxes = result.boxes
        for box in boxes:
            if box.conf >= confidence_threshold:
                x, y, w, h = int(box.xyxy[0][0]), int(box.xyxy[0][1]), int(box.xyxy[0][2] - box.xyxy[0][0]), int(box.xyxy[0][3] - box.xyxy[0][1])
                calculatePositionForDetectedPerson(frame, x, y, h, w)
                cv2.rectangle(frame, (x, y), (x + w, y + h), colorRed, 2)

    # Show in the screen
    cv2.imshow('Drone Human Tracking', frame)

    # Quit with 'q' 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
