import streamlit as st
import datetime

from cloud.Streaming_cloud_storage import *

# cv_window_titles = ["first", "second", "third", "fourth"]


def st_multi_window_cloud(camslist):
    names = camslist
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
                # Streaming_cloud_storage_2(camslist, frames_per_videoclip, path)

        # if cv2.waitKey(1) & 0xFF == ord("q"):
        #     break

    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()
    return
