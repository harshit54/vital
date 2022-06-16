import cv2
import dlib
import numpy as np
import pyautogui as pag

from src.utils import diff_calculator, shape_to_np, pupil_tracker
from src.display import eye_on_mask, center_of_eye, show_eye
from src.control import Context, Scroll

mouse = Context(Scroll())
pag.FAILSAFE = False


def changeState():
    mouse.changeState()


def changePrecision():
    mouse.changePrecision()


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('public/shape_68.dat')

left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]


def doNothing(x):
    pass


cap = None


def startTracker():
    cap = cv2.VideoCapture(1)

    ret, img = cap.read()
    thresh = img.copy()

    cv2.namedWindow('image')
    kernel = np.ones((9, 9), np.uint8)

    cv2.createTrackbar('threshold', 'image', 0, 255, doNothing)

    mouse.center_mouse()
    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 1)
        for rect in rects:

            shape = predictor(gray, rect)
            shape = shape_to_np(shape)

            mask = np.zeros(img.shape[:2], dtype=np.uint8)

            mask = eye_on_mask(mask, left, shape)

            mask = eye_on_mask(mask, right, shape)

            center_of_eye(img, shape)

            mask = cv2.dilate(mask, kernel, 5)
            eyes = cv2.bitwise_and(img, img, mask=mask)
            mask = (eyes == [0, 0, 0]).all(axis=2)
            eyes[mask] = [255, 255, 255]

            mid = (shape[42][0] + shape[39][0]) // 2  # Mid point between two eyes

            eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
            threshold = cv2.getTrackbarPos('threshold', 'image')
            _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
            thresh = cv2.erode(thresh, None, iterations=2)  # 1
            thresh = cv2.dilate(thresh, None, iterations=4)  # 2
            thresh = cv2.medianBlur(thresh, 3)  # 3
            thresh = cv2.bitwise_not(thresh)
            pupil_tracker(thresh, mid, img)
            show_eye(img, shape)
            x, y = diff_calculator(thresh, mid, img, shape)
            mouse.move(x, y)

        cv2.imshow('eyes', img)
        cv2.imshow("image", thresh)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def stopTracker():
    cap.release()
    cv2.destroyAllWindows()
