import streamlit as st
import pandas as pd
import cv2

from multiprocessing import Process
import sys

from vc.vc_streaming_cloud import *

# from cloud.cloud_test import *

from cloud_test2 import *


def form_Streaming_cloud_storage(username, path):
    print("Iam Strreaming_cloud_storage in input form")

    with st.form(key="ip_cctv_connect0"):
        ipcam1 = st.text_input("Camera1", "ip address1")
        ipcam2 = st.text_input("Camera2", "ipaddress2")
        ipcam3 = st.text_input("Camera3", "ipaddress3")
        frames_per_videoclip = st.number_input("frames per c;lip")

        connect1 = st.form_submit_button(label="Connect99")

    disconnect = st.button("Disconnect99")
    camslist = [ipcam1, ipcam2, ipcam3]
    if connect1:
        kk(camslist)

    return
