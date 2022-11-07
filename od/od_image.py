import streamlit as st
import pandas as pd
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os
import time, sys
import urllib.request
import urllib
import cv2
import numpy as np
import time
import sys

classes = []
confidence_value = 0.001


def img_od(img, confidence_value):
    height, width, channels = img.shape

    with open("od/yolo/coconames.txt", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net = cv2.dnn.readNet("od/yolo/yolov3-tiny.weights", "od/yolo/yolo3.cfg")

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    for b in blob:
        for n, img_blob in enumerate(b):
            pass

    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_value:
                # onject detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # cv2.circle(img,(center_x,center_y),10,(0,255,0),2)

                # rectangle co-ordinaters
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                boxes.append([x, y, w, h])  # put all rectangle areas
                confidences.append(
                    float(confidence)
                )  # how confidence was that object detected and show that percentage
                class_ids.append(class_id)  # name of the object tha was detected

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.6)
    font = cv2.FONT_HERSHEY_PLAIN

    frame_window1_od = st.image([])

    # print(boxes)
    # print(len(boxes))
    lbls = []
    for i in range(len(boxes)):

        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            img1 = cv2.rectangle(img, (x, y), (x + w, y + h), color, 4)
            img2 = cv2.putText(img1, label, (x, y + 30), font, 1, (255, 255, 255), 4)

            # frame_window1_od.image(img2)
            lbls.append(label)

    # frame_window1_od.image(img2)

    # cv2.imshow("Imagewew", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # print(lbls)
    total_labels = len(lbls)
    return lbls, total_labels
