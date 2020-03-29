# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 08:02:44 2020

@author: AnujaBabu
"""


import cv2
catPath = "haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(catPath)
img = cv2.imread("result.jpg")  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor= 1.02,
    minNeighbors=3,
    minSize=(150, 150),
    flags=cv2.CASCADE_SCALE_IMAGE
)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.imshow('Cat?', img)
cv2.imwrite("cat33.jpg",img)
c = cv2.waitKey(0)