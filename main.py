import streamlit as st
import pandas as pd
import cv2

import streamlit as st
import streamlit_book as stb

from multiprocessing import Process
import sys
import hashlib

# from forms.form_only_streaming import *
# from forms.form_streaming_od import *
# from forms.form_streaming_cloud import *



# from device_camera import *
# from streamlit_webrtc import webrtc_streamer

# from device_main import *
# from device_od import *
# from od_tracking import *

# from fr import *
# from g_auth import *
# from options import *

conf_thres_drift = 0.75
conf_thres = 0.50
fps_drop_warn_thresh = 10

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management
import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()
# DB  Functions
def create_usertable():
    c.execute("CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)")


def add_userdata(username, password):
    c.execute(
        "INSERT INTO userstable(username,password) VALUES (?,?)", (username, password)
    )
    conn.commit()


def login_user(username, password):
    c.execute(
        "SELECT * FROM userstable WHERE username =? AND password = ?",
        (username, password),
    )
    data = c.fetchall()
    return data


def view_all_users():
    c.execute("SELECT * FROM userstable")
    data = c.fetchall()
    return data


def main():
    st.image("./logo.png")
    st.title("Avistos Innovative Solutions")

    menu = ["Home", "Login", "SignUp", "Logout","Google-Login"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Ip Camera System")

    elif choice == "Google-Login":
        st.subheader("Google Login")
        new_glogin()
      

    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")

        st.sidebar.checkbox("Login-As- Avistos")
        st.sidebar.checkbox("Login-As- Client")

        if st.sidebar.checkbox("Login"):

            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                # st.set_page_config(layout="centered")



                stb.set_book_config(
                        menu_title="User Home-Page",
                        menu_icon="User",
                        options=[
                                "1_Welcome Profile",
                                "2_Face Registration",
                                "3_Device Camera",
                                "4_Device Camera_with_OD",
                                "5_Device Camera_with_OD_Tracking",
                                "6_Device Camera_with_Saving_To_Cloud",
                                "7_Only Streaming",
                                "8_Streaming with OD",
                                "9_Streaming With OD and Tracking",
                                "10_offline video creation and saving",
                                "11_Streaming with OD and cloud storage",
                                "12_Snowflake Integration",
                                "13_Nvr_Dvr_connection",
                                "14_logout"
                            ], 
                        paths=[
                            "welcome_profile/home.py",
                            "face_recognition/fr.py", 
                            "device_camera/device_camera.py", 
                            "device_camera_od/device_camera_od.py", 
                            "device_camera_od_tracking/device_camera_od_tracking.py", 
                            "device_camera_save_cloud/device_camera_save_cloud.py", 
                            "only_streaming/stream.py",
                            "streaming_od/streaming_od.py",
                            "streaming_od_tracking/streaming_od_tracking.py",
                            "offline_video_creation/offline_video.py", 
                            "streaming_od_cloud/streaming_od_cloud.py",
                            "snowflake/snowflake_home.py",
                            "nvr_dvr_connection/nvr_home.py",
                            "login_logout/logout.py",
                  
                            
                            ],
                        save_answers=False,
                        styles={
                            "nav-link": {"--hover-color": "#fde8ec"},
                            "nav-link-selected": {"background-color": "#DC143C"},
                        }
                        )



       

                    
        elif choice == "Logout":
            login_user.logout("Logout", "main")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")


if __name__ == "__main__":
    main()




# Set wide display
