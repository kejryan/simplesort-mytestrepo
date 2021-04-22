
###############################################################################

import time
import cv2


import PIL
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import cv2

import pigpio


def get_image_from_camera(camera):
    """Read an image from the camera"""
    if camera:
        ret, frame = camera.read()
        if not ret:
            raise Exception("your capture device is not returning images")
        return frame
    return None


def main():

    pi1 = pigpio.pi() #create instance of pigpio.pi class
    pi1.write(4, 0)
    pi1.write(5, 0)

    # Open the video camera. To use a different camera, change the camera
    # index.
    camera = cv2.VideoCapture(0)

    img_height = 224
    img_width = 224


    #show camera and prompt to take picture
    while (cv2.waitKey(1) & 0xFF) == 0xFF:

        image = get_image_from_camera(camera)
        cv2.imshow("SimpleSort: press any key to take picture", image)

    # Get an image from the camera.
    image = get_image_from_camera(camera)

    resized_img = cv2.resize(image, (img_height, img_width))

    # Display the image
    cv2.imshow("SimpleSort", image)

    X = np.array(resized_img)
    X = X / 255

    # increases dimension by 1
    X = tf.expand_dims(X, 0) # Create a batch
    #print(X.shape)

    model = tf.keras.models.load_model('model.tflite')

    prediction = model.predict(X)
    score = tf.nn.softmax(prediction[0])

    class_names = ["cardboard", "compost", "glass", "metal", "paper", "plastic", "trash"]

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
   
    cat = np.argmax(score)

    if cat == 0 or cat == 2 or cat == 3 or cat == 4 or cat == 5:
        print("recycle, gpio 4")
        pi1.write(4, 1)

    elif cat == 1:
        print("compost, gpio 5")
        pi1.write(5, 1)

    elif cat == 6:
        print("trash, gpio 4 & gpio 5")
        pi1.write(4, 1)
        pi1.write(5, 1)
        

if __name__ == "__main__":
    main()
