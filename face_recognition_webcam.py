import face_recognition
import cv2
from Face import Face

def drawRectangle():
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (blue, green, red), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (blue, green, red), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

#Carrega a camera
video_capture = cv2.VideoCapture(0)

#Cria os objetos
jonas = Face(face_recognition.load_image_file("image.jpg"), 0, 255, 0, 'Jonas')
lucas = Face(face_recognition.load_image_file("image1.jpg"), 0, 255, 0, 'Lucas')
juan = Face(face_recognition.load_image_file("image2.jpg"), 0, 255, 0, 'Juan')

faces = [juan, lucas, jonas]
#x = len(faces) -> retorna o tamanho do array

encoded_images = []
face_locations = []
face_encodings = []
process_this_frame = True

for face in faces:
    image_face_encoding = face_recognition.face_encodings(face.getFoto())[0]
    encoded_images.append(image_face_encoding)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(encoded_images, face_encoding)
            if match[face_encodings.index(face_encoding)]:
                name = faces[face_encodings.index(face_encoding)].getNome()
                red = faces[face_encodings.index(face_encoding)].getRed()
                green = faces[face_encodings.index(face_encoding)].getGreen()
                blue = faces[face_encodings.index(face_encoding)].getBlue()

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    drawRectangle()

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
