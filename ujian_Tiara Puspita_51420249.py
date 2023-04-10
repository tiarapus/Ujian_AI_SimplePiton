import cv2


cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    _, frame = cam.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    heigt, width, _ = frame.shape

    cx = int(width/2)
    cy = int(heigt/2)

    #mengambil nilai dari pixel warna
    pixel_center = hsv_frame[cy,cx]
    hue = pixel_center[0]
    saturation = pixel_center[1]
    value = pixel_center[2]

    color = "Unknown"
    if hue == 0 | saturation == 0 :
        color = "White"
    elif value < 50 :
        color = "Black"
    elif saturation < 50 :
        color = "Grey"    
    elif hue < 5 :#  0 < Merah < 5
        color = "Red"
    elif hue < 20 :#  5 < Orange < 20
        color = "ORANGE"
    elif hue < 30 :#  20 < Kuning < 30
        color = "Yellow"
    elif hue < 70 :#  30 < Hijau < 70
        color = "Green"
    elif hue < 125 :#  70 < Biru < 125
        color = "Blue" 
    elif hue < 145 :#  125 < Ungu < 145
        color = "Purple"
    elif hue < 170 :#  145 < orange < 170
        color = "PINK"   
    else :
       color = "MERAH"       

    pixel_center_bgr = frame[cy,cx]

    b = int(pixel_center_bgr[0])
    g = int(pixel_center_bgr[1])
    r = int(pixel_center_bgr[2])

    print(pixel_center)
    cv2.putText(frame, color, (cx - 100,cy - 150), 0,1.5, (b, g, r), 8)
    cv2.circle(frame, (cx,cy), 5, (25, 25, 25), 0)

    cv2.imshow("Color Detection", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cam.release()
cv2.destroyAllWindows()