import numpy as np
import cv2
import streamlit as st
from od.od_image import *


def st_multi_window_od(camerascc, confidence_value):

    names = camerascc
    window_titles = []
    for i in range(len(names)):
        # st.write("Streaming Camera :")
        # st.write(i)
        frame_window = st.image([])
        window_titles.append(frame_window)
    cap = [cv2.VideoCapture(i) for i in names]

    frames = [None] * len(names)
    gray = [None] * len(names)
    ret = [None] * len(names)

    while True:

        for i, c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read()

        font = cv2.FONT_HERSHEY_PLAIN
        for i, f in enumerate(frames):

            if ret[i] is True:
                x = 50
                y = 50
                gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
                lbls, total_labels = img_od(gray[i], confidence_value)
                gg = "count : " + str(total_labels)
                gray[i] = cv2.putText(
                    gray[i], gg, (x + 30, y + 60), font, 1, (255, 255, 255), 4
                )
                window_titles[i].image(gray[i])

        # for k, f in enumerate(frames):
        #     if ret[k] is True:
        #         gray[k] = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
        #         image_od = img_od(f)
        #         window_titles[i].image(image_od)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()
    return
