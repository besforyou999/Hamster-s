# aruco marker 주사위

import numpy as np
import cv2
import cv2.aruco as aruco
import winsound
from roboid import *

def sound(i):
    sol = {'do': 261, 're': 293, 'mi': 329, 'pa': 349, 'sol': 391, 'ra': 440, 'si': 493}
    mel = ['do', 'mi', 'mi', 'mi', 'sol', 'sol', 're', 'pa', 'pa']
    dur = [4, 4, 2, 4, 4, 2, 4, 4, 2]
    mel2 = ['si', 're']
    dur2 = [1, 1]
    music = zip(mel, dur)
    music2 = zip(mel2, dur2)

    if i == 1:
        for melody, duration in music2:
            winsound.Beep(sol[melody], 100 // duration)
    elif i == 2:
        for melody, duration in music:
            winsound.Beep(sol[melody], 1000 // duration)

# 노트북 웹캠이 있다면 VideoCapture의 인자를 1로, 없다면 0으로
cam = cv2.VideoCapture(1)
dictionary = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
hamster0 = HamsterS(0)
hamster1 = HamsterS(1)
counter = 0
wait_time = 30
occupation = 0
hamster_speed = 80

# hamster 0 first
turn = 1

while True:
    _, image = cam.read()
    image = image[35:595, 110:540]
    image = cv2.rectangle(image, (105,115), (325, 325), (255,0,0), 1, cv2.LINE_8)
    corners, ids, rejected = aruco.detectMarkers(image, dictionary)

    counter += 1
    #sound(1)
    wait(100)

    num_image = np.zeros((320, 320, 3), np.uint8)

    cv2.imshow('num_image', num_image)
    cv2.imshow('image', image)

    if ids is None:
        occupation = 0

    if counter > wait_time and occupation == 0 and ids is not None:
        aruco.drawDetectedMarkers(image, corners, borderColor=(0, 0, 255))
        if ids[0, 0] == 0:
            cv2.putText(num_image, "1", (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 8, cv2.LINE_AA)
            winsound.Beep(100, 50)
            if turn == -1 :
                hamster0.wheels(hamster_speed)
            elif turn == 1 :
                hamster1.wheels(hamster_speed)
            wait(500)
            hamster0.stop()
            hamster1.stop()
        elif ids[0, 0] == 1:
            cv2.putText(num_image, "2", (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 8, cv2.LINE_AA)
            winsound.Beep(400, 50)
            if turn == -1:
                hamster0.wheels(hamster_speed)
            elif turn == 1:
                hamster1.wheels(hamster_speed)
            wait(1000)
            hamster0.stop()
            hamster1.stop()
        elif ids[0, 0] == 2:
            cv2.putText(num_image, "3", (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 8, cv2.LINE_AA)
            winsound.Beep(700, 50)
            if turn == -1:
                hamster0.wheels(hamster_speed)
            elif turn == 1:
                hamster1.wheels(hamster_speed)
            wait(1500)
            hamster0.stop()
            hamster1.stop()
        elif ids[0, 0] == 3:
            cv2.putText(num_image, "4", (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 8, cv2.LINE_AA)
            winsound.Beep(1000, 50)
            if turn == -1:
                hamster0.wheels(hamster_speed)
            elif turn == 1:
                hamster1.wheels(hamster_speed)
            wait(2000)
            hamster0.stop()
            hamster1.stop()
        elif ids[0, 0] == 4:
            cv2.putText(num_image, "5", (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 8, cv2.LINE_AA)
            winsound.Beep(1300, 50)
            if turn == -1:
                hamster0.wheels(hamster_speed)
            elif turn == 1:
                hamster1.wheels(hamster_speed)
            wait(2500)
            hamster0.stop()
            hamster1.stop()
        elif ids[0, 0] == 5:
            cv2.putText(num_image, "6", (60, 250), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 8, cv2.LINE_AA)
            winsound.Beep(1600, 50)
            if turn == -1:
                hamster0.wheels(hamster_speed)
            elif turn == 1:
                hamster1.wheels(hamster_speed)
            wait(3000)
            hamster0.stop()
            hamster1.stop()

        turn *= -1
        occupation = 1
        counter = 0
        cv2.imshow('num_image', num_image)
        cv2.imshow('image', image)
        #cv2.waitKey(100)
        sound(2)
        #wait(1000)

    if counter > wait_time + 30 or occupation == 1:
        empty_image = np.full((320, 320, 3), (0, 0, 0), np.uint8)
        cv2.putText(empty_image, "Roll the Dice", (60, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', empty_image)

        cv2.waitKey(100)
        sound(1)
        wait(1000)
        counter = 0
        continue

    if cv2.waitKey(1) == 27:
        break



#def handle_movement(number):

