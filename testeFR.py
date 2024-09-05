import cv2
import face_recognition as fr

myImg = fr.load_image_file("./pessoas/imgCadastro.jpeg")
myImg = cv2.cvtColor(myImg, cv2.COLOR_BGR2RGB)

testImg = fr.load_image_file("./pessoas/pessoa-interessante.png")
testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2RGB)

face_location = fr.face_locations(myImg)[0]
face_test_location = fr.face_locations(testImg)[0]
# print(face_location)

cv2.rectangle(myImg, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (0, 255, 0), 2)

myEncode = fr.face_encodings(myImg)[0]
testEncode = fr.face_encodings(testImg)[0]

comparing = fr.compare_faces([myEncode], testEncode)

if(comparing[0]):
    print("É a Fabiana")
else:
    print("Não é")

# cv2.circle(myImg, (face_location[3], face_location[0]), radius=0, color=(0, 0, 255), thickness=5)
# cv2.circle(myImg, (face_location[1], face_location[2]), radius=0, color=(0, 255, 0), thickness=5)
# cv2.circle(myImg, (face_location[2], face_location[2]), radius=0, color=(255, 0, 0), thickness=5)
# cv2.circle(myImg, (face_location[3], face_location[3]), radius=0, color=(0, 255, 255), thickness=5)

cv2.imshow('Fabiana', myImg)
cv2.waitKey(0)

#top right bottom left