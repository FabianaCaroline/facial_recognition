import cv2
import face_recognition as fr
from engine import detecta_face, procura_conhecido

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

captura = detecta_face(frame)
face_loc = 0

if (captura[0]):
   face_loc = fr.face_locations(frame)[0]
   result = procura_conhecido(captura[1])

   cv2.rectangle(frame, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 0), 2)
   cv2.putText(frame, result, (face_loc[3], (face_loc[2] + 30)), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

else:
  print("Não foi possível identificar um rosto")

if not ret:
  cap.release()
  cv2.destroyAllWindows()     


cv2.imshow("Frame", frame)
cv2.waitKey(0)