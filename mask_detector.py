import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

class MaskDetector:
    def __init__(self):
        self.model = load_model('model/saved_model.h5')
        self.face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)  # Start video capture

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return b''

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            face = frame[y:y + h, x:x + w]
            resized_face = cv2.resize(face, (150, 150))
            img_array = np.expand_dims(resized_face, axis=0) / 255.0
            prediction = self.model.predict(img_array)

            if prediction[0][0] > 0.5:
                label = 'Mask'
                color = (0, 255, 0)
            else:
                label = 'No Mask'
                color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
