import cv2
import face_recognition as fr

rostos_conhecidos = [("Elon-Musk.jpg", "Elon Musk"), ("imgCadastro.jpeg", "Fabiana"), ("pessoa-interessante.png", "Alice")]

def detecta_face(frame):
    rosto = fr.face_encodings(frame)
    
    if(len(rosto) > 0):
        return True, rosto[0]
    return False

def procura_conhecido(face_encoding):
    cont = 0

    for p in rostos_conhecidos:
        face = fr.load_image_file(f"./pessoas/{p[0]}")
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        face = fr.face_encodings(face)[0]

        if(fr.compare_faces([face_encoding], face)[0]):
            cont = 1
            return f"Olá, {p[1]}!"

    if (cont > 0):
        return "Usuário não identificado"