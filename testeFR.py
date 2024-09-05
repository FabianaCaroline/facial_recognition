import cv2
import face_recognition as fr

myImg = fr.load_image_file("./pessoas/imgCadastro.jpeg")

cv2.imshow('Fabiana', myImg)
cv2.waitKey(0)