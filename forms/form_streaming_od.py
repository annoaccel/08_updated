import streamlit as st
import pandas as pd
import cv2

from vc.vc_streaming_od import *



def streaming_od():
    
    with st.form(key="ip_cctv_connect0"):
        ipcam1 = st.text_input("Camera1", "ip address1")
        ipcam2 = st.text_input("Camera2", "ipaddress2")
        ipcam3 = st.text_input("Camera3", "ipaddress3")
        confidence_value = st.number_input("enter the confidence value")
        connect1 = st.form_submit_button(label="Connect0")

    disconnect = st.button("Disconnect!")
    camslist = [ipcam1, ipcam2, ipcam3]

    if connect1:
        st_multi_window_od(camslist, confidence_value)

    return
