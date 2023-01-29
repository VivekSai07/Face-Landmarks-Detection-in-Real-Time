import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r"D:\\Coding\\Opencv Computer Vision\\Face Landmarks in Real-Time\\Videos\\production ID_4736800.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 5, (1280,720))

pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=5)
# drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=5)


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLMS in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLMS, mpFaceMesh.FACEMESH_CONTOURS)

            for id, lm in enumerate(faceLMS.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id, x, y)

    b = cv2.resize(img, (1200, 780), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
    out.write(b)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(b, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow("Image", b)
    cv2.waitKey(1)




