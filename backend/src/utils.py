import numpy as np
from src.display import center_of_eye
import cv2


def shape_to_np(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)
    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-co~ordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    # return the list of (x, y)-coordinates
    return coords


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(0.5)


def pupil_tracker(thresh, mid, img):
    left = contouring(thresh[:, 0:mid], mid, img)
    right = contouring(thresh[:, mid:], mid, img, True)
    return (left, right)


def diff_calculator(thresh, mid, img, shape):
    left_pupil, right_pupil = pupil_tracker(thresh, mid, img)
    try:
        left_eye, right_eye = center_of_eye(img, shape)
        move_x = ((left_pupil[0] - left_eye[0]) + (right_pupil[0] - right_eye[0])) / 2
        move_y = ((left_pupil[1] - left_eye[1]) + (right_pupil[1] - right_eye[1])) / 2
        return (move_x, move_y)
    except:
        return (0, 0)


def contouring(thresh, mid, img, right=False):
    cnts, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    try:
        cnt = max(cnts, key=cv2.contourArea)
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        if right:
            cx += mid
        cv2.circle(img, (cx, cy), 4, (172, 255, 0), 2)
        return (cx, cy)
    except:
        pass
