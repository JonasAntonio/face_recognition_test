import face_recognition
import cv2
from Face import Face

#Cria os objetos
jonas = Face(face_recognition.load_image_file("image.jpg"), 0, 255, 0, 'Jonas')
lucas = Face(face_recognition.load_image_file("image1.jpg"), 0, 255, 0, 'Lucas')
juan = Face(face_recognition.load_image_file("image2.jpg"), 0, 255, 0, 'Juan')

faces = [jonas, lucas, juan]

#x = len(faces) -> retorna o tamanho do array

for face in faces:
    image_face_encoding = face_recognition.face_encodings(face.getFoto())[0]
