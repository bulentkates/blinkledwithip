import cv2
import serial
import numpy as np
import time
ser = serial.Serial('COM6', 9600, timeout=1)
cap = cv2.VideoCapture(0)
red_light_detected = False
while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    if cv2.countNonZero(green_mask) > 1000:
        ser.write(b'1')
        print("Green")
        red_light_detected = False  
    elif cv2.countNonZero(red_mask) > 1000 and not red_light_detected:
        ser.write(b'2')
        print("Red")
        red_light_detected = True  
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
ser.close()
cap.release()
cv2.destroyAllWindows()
