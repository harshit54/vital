import numpy as np
import cv2
import utils


def eye_on_mask(mask, side, shape):
    points = [shape[i] for i in side]
    points = np.array(points, dtype=np.int32)
    mask = cv2.fillConvexPoly(mask, points, 255)
    return mask


def center_of_eye(img, shape):
    left_eye = shape[36:42]
    x_left = sum(left_eye[i][0] for i in range(6)) / 6
    y_left = sum(left_eye[i][1] for i in range(6)) / 6
    left = (x_left, y_left)

    right_eye = shape[42:48]
    x_right = sum(right_eye[i][0] for i in range(6)) / 6
    y_right = sum(right_eye[i][1] for i in range(6)) / 6
    right = (x_right, y_right)

    cv2.circle(img, (int(x_left), int(y_left)), 2, (255, 0, 255), -1)
    cv2.circle(img, (int(x_right), int(y_right)), 2, (255, 255, 0), -1)

    return (left, right)


def eyeLeft(shape):
    p1, p2, p3, p4, p5, p6 = shape[37], shape[38], shape[39], shape[40], shape[41], shape[42]
    eyeAspectRatio = (utils.dist(p2, p6) + utils.dist(p3, p5)
                      ) / (2 * utils.dist(p1, p4))
    return eyeAspectRatio


def eyeRight(shape):
    p1, p2, p3, p4, p5, p6 = shape[43], shape[44], shape[45], shape[46], shape[47], shape[48]
    eyeAspectRatio = (utils.dist(p2, p6) + utils.dist(p3, p5)
                      ) / (2 * utils.dist(p1, p4))
    return eyeAspectRatio


def show_eye(img, shape):
    for (x, y) in shape[36:48]:
        cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
