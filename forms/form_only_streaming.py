import streamlit as st
import cv2

from vc.vc_streaming import *

def only_streaming():
    # st.image("./logo.png")
    # st.title("Avistos Innovative Solutions")

    with st.form(key="ip_cctv_connect0"):
        ipcam1 = st.text_input("Camera1", "ip address1")
        ipcam2 = st.text_input("Camera2", "ipaddress2")
        ipcam3 = st.text_input("Camera3", "ipaddress3")
        connect1 = st.form_submit_button(label="Connect0")
    disconnect = st.button("Disconnect!")


    camslist = [ipcam1, ipcam2, ipcam3]
    if connect1:
        st_multi_window(camslist)

    return camslist
