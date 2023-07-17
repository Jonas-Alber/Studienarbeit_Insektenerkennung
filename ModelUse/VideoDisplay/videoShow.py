import cv2
import tensorflow as tf
import numpy as np
import os
import random
import math

CURRENT_PATH = os.getcwd()
MODEL_PATH = os.path.join(CURRENT_PATH, r"tfModel")
VIDEO_PATH = os.path.join(CURRENT_PATH, r"videos")

lastPredictionList = [[], [], [], []]
maxListElements = 3

def getImageBorder(prediction):
    for index, value in enumerate(prediction[1][0]):
        lastPredictionList[index].append(float(value))

    returnList = [0, 0, 0, 0]
    for index, element in enumerate(lastPredictionList):
        counterValue = 0
        for i in element:
            counterValue += i
        returnList[index] = float(counterValue / len(element))
        if len(element) > maxListElements:
            element.pop(0)

    return returnList

def getObjectData(prediction):
    highValue = 0
    indexValue = None
    for index, value in enumerate(prediction[2][0]):
        if value > highValue:
            highValue = value
            indexValue = index
    return (indexValue, float(highValue))

def on_window_closed(event, x, y, flags, param):
    if event == cv2.WINDOW_CLOSE:
        input("Hi")
        cv2.destroyAllWindows()
        print("Fenster wurde geschlossen")

# Laden des Videos
videoList = []
for element in os.listdir(VIDEO_PATH):
    filename, file_extension = os.path.splitext(element)
    if file_extension == ".mp4":
        videoList.append(os.path.join(VIDEO_PATH, element))
random.shuffle(videoList)
output_path = r"D:\Studienarbeit\VideoDisplay\dump\bee_test.mp4"
model = tf.keras.models.load_model(MODEL_PATH)
doLoop = True
classList = ["Other Insects", "Bee", "Bumblebee", "Vespula"]
showText = False
while doLoop:
    for vidPath in videoList:
        video_capture = cv2.VideoCapture(vidPath)

        # Erstellen des VideoWriters für die Ausgabe
        output_fps = video_capture.get(cv2.CAP_PROP_FPS)  # Framerate des Eingabevideos übernehmen
        output_size = (
            int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec für das Ausgabevideo
        video_writer = cv2.VideoWriter(output_path, fourcc, output_fps, output_size)

        # Blue color in BGR
        color = (255, 0, 0)
        min_window_width = 1920
        min_window_height = 1080

        # Line thickness of 2 px
        thickness = 2
        # Echtzeit-Bearbeitung und Ausgabe der Frames
        while doLoop:  # video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret:
                break
            # Video-Frame an die Größe des Fensters anpassen
            height, width, _ = frame.shape
            resized_image = cv2.resize(frame, (128, 128))
            np_data = np.array(resized_image).astype('float32') / 255
            np_image = np.expand_dims(np_data, axis=0)
            prediction = model.predict(np_image)

            xMin, yMin, xMax, yMax = getImageBorder(prediction)
            xMin = int(xMin * width)
            yMin = int(yMin * height)
            xMax = int(xMax * width) + xMin
            yMax = int(yMax * height) + yMin
            startPos = (xMin, yMin)
            endPos = (xMax, yMax)

            classIndex, classPercentage = getObjectData(prediction)
            expo = math.floor(math.log10(abs(classPercentage)))
            if expo < -2:
                classPercentage *= (10 * -expo - 2)
            classPercentage = round((classPercentage * 100), 2)
            text = f"{classPercentage}% {classList[classIndex]}"
            rec_frame = cv2.rectangle(frame, startPos, endPos, color, thickness)
            font_scale = 1.0
            font = cv2.FONT_HERSHEY_SIMPLEX
            if showText:
                rec_frame = cv2.putText(rec_frame, text, (10, 40), font, font_scale, color, thickness)

            key = cv2.waitKey(1)
            if key == ord("q"):  # nächstes Video
                break
            elif key == ord("t"):  # Programm beenden
                doLoop = False
                break
            elif key == ord("s"):  # Toggeln der Klassifikationsanzeige
                showText = not showText

            window_width = max(cv2.getWindowProperty("Video", cv2.CAP_PROP_FRAME_WIDTH), min_window_width)
            window_height = max(cv2.getWindowProperty("Video", cv2.CAP_PROP_FRAME_HEIGHT), min_window_height)

            scaled_frame = cv2.resize(rec_frame, (int(window_width), int(window_height)))
            
            # Text über das Video legen
            cv2.putText(scaled_frame, "Tastenfunktionen", (10, 40), font, font_scale, color, thickness)
            cv2.putText(scaled_frame, "q: springe ein Video weiter", (10, 80), font, font_scale, color, thickness, cv2.LINE_AA, False)
            cv2.putText(scaled_frame, "t: Programm beenden", (10, 120 ), font, font_scale, color, thickness, cv2.LINE_AA, False)
            cv2.putText(scaled_frame, "s: Klassifikationsanzeige toggeln", (10, 160), font, font_scale, color, thickness, cv2.LINE_AA, False)

            cv2.imshow("Live-Darstellung", scaled_frame)
            video_writer.write(rec_frame)

            if cv2.getWindowProperty('Live-Darstellung', 0) < 0:
                video_capture.release()
                video_writer.release()
                cv2.destroyAllWindows()

video_capture.release()
video_writer.release()
cv2.destroyAllWindows()
