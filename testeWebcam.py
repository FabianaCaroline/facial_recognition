import cv2
from engine import detecta_face, procura_conhecido

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

captura = detecta_face(frame)

if (captura[0]):
  print(procura_conhecido(captura[1]))

else:
  print("Não foi possível identificar um rosto")

if not ret:
  cap.release()
  cv2.destroyAllWindows()     

cv2.imshow("Frame", frame)
cv2.waitKey(0)