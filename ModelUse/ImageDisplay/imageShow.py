import cv2
import tensorflow as tf
import numpy as np
import os
import random
import math
import time

CURRENT_PATH = os.getcwd()
MODEL_PATH = os.path.join(CURRENT_PATH, r"tfModel")
IMAGE_PATH = os.path.join(CURRENT_PATH, r"images")

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

# Laden der Bilder
imageList = []
for element in os.listdir(IMAGE_PATH):
    filename, file_extension = os.path.splitext(element)
    if file_extension in [".jpg", ".png"]:
        imageList.append(os.path.join(IMAGE_PATH, element))
random.shuffle(imageList)
output_path = r"D:\Studienarbeit\VideoDisplay\dump\bee_test.mp4"
model = tf.keras.models.load_model(MODEL_PATH)
classList = ["Other Insects", "Bee", "Bumblebee", "Vespula"]
showText = False

index = 0  # Aktueller Bildindex

while True:
    imagePath = imageList[index]
    image = cv2.imread(imagePath)
    image_height, image_width, _ = image.shape

    # Anpassen der Größe des Bildes
    resized_image = cv2.resize(image, (128, 128))
    np_data = np.array(resized_image).astype('float32') / 255
    np_image = np.expand_dims(np_data, axis=0)
    prediction = model.predict(np_image)

    xMin, yMin, xMax, yMax = getImageBorder(prediction)
    xMin = int(xMin * image_width)
    yMin = int(yMin * image_height)
    xMax = int(xMax * image_width) + xMin
    yMax = int(yMax * image_height) + yMin
    startPos = (xMin, yMin)
    endPos = (xMax, yMax)

    classIndex, classPercentage = getObjectData(prediction)
    expo = math.floor(math.log10(abs(classPercentage)))
    if expo < -2:
        classPercentage *= (10 * -expo - 2)
    classPercentage = round((classPercentage * 100), 2)
    text = f"{classPercentage}% {classList[classIndex]}"
    rec_frame = cv2.rectangle(image, startPos, endPos, (255, 0, 0), 2)

    # Skalieren des Texts basierend auf der Bildgröße
    text_scale = 0.2
    text_thickness = 1
    text_font = cv2.FONT_HERSHEY_SIMPLEX
    text_size, _ = cv2.getTextSize(text, text_font, text_scale, text_thickness)
    text_width = text_size[0]
    text_height = text_size[1]

    # Position des Texts in der oberen linken Ecke berechnen
    text_position = (int(0.02 * image_width), int(0.05 * image_height) + text_height)

    if showText:
        rec_frame = cv2.putText(rec_frame, text, text_position, text_font, text_scale, (255, 0, 0), text_thickness)

    cv2.imshow("Bild-Analyse", rec_frame)

    key = cv2.waitKey(3000)  # 3 Sekunden anzeigen

    if key == ord("t"):  # Programm beenden
        break
    elif key == ord("s"):  # Toggeln der Klassifikationsanzeige
        showText = not showText

    # Inkrementieren des Index und Zurücksetzen, wenn das Ende der Liste erreicht ist
    index += 1
    if index >= len(imageList):
        index = 0

cv2.destroyAllWindows()
