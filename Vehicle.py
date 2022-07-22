import os
import keras_datasets
import cv2
cap = cv2.VideoCapture(1)
while True:
    frame,ret = cap.read()
    cv2.imshow('dnndj',frame)