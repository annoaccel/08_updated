import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

# st.image("./logo.png")
# st.title("Avistos Innovative Solutions")

st.header("Welcome To Device Camera")

threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
threshold2 = st.slider("Threshold2", min_value=1, max_value=800, step=1, value=200)


def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    # img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


def mystream():

    threshold1 = st.slider("Threshold1", min_value=0, max_value=8000, step=1, value=100)
    threshold2 = st.slider("Threshold2", min_value=1, max_value=1000, step=1, value=200)

# webrtc_streamer(key="example", video_frame_callback=callback)

webrtc_streamer(
        key="example",
        video_frame_callback=callback,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    )


mystream()
