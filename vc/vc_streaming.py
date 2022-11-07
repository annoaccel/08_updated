import numpy as np
import cv2
import streamlit as st


cv_window_titles = ["first", "second", "third", "fourth"]


def st_multi_window(camerascc):

    names = camerascc
    window_titles = []
    for i in range(len(names)):
        st.write("Streaming Camera :")
        st.write(i)
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

        for i, f in enumerate(frames):
            if ret[i] is True:
                gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)

                window_titles[i].image(gray[i])

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()

    return
