import streamlit as st
import streamlit_book as stb


st.title("Avistos Ip Camera Stream")

# stb.set_book_config(
#                 menu_title="Admin",
#                 menu_icon="public",
#                 options=[
#                     "My-Profile", 
#                     "od-home", 
#                     "Logout", 
#                     ], 
#                 paths=[
#                     "streaming/od/od_home.py", 
#                     "streaming/od/od_home.py", 
#                     "private/logout.py", 
#                     ],
#                 save_answers=False,
#                 styles={
#                     "nav-link": {"--hover-color": "#fde8ec"},
#                     "nav-link-selected": {"background-color": "#DC143C"},
#                 }
#                 )






# prod_options = st.radio("Select Product Options",("Welcome",
#                             "Face Registration",

#                             "Device Camera",
#                             "Device Camera_with_OD",
#                             "Device Camera_with_OD_Tracking",
#                             "Device Camera_with_Saving_To_Cloud",
#                             "Only Streaming",
#                             "Streaming with OD",
#                             "offline video creation and saving",
#                             "Streaming with OD and cloud storage",
#                             "Streaming With OD and Tracking",)
                            
#                         ),
                    
# if prod_options == "welcome":
#     pass
# elif prod_options == "Face Registration":
#                         fr(use
                       
                        # print("Welcome to Avistos")

                    # elif prod_options == "Device Camera":
                    #     mystream(username)
                    # elif prod_options == "Device Camera_with_OD":
                    #     device_main()
                    # elif prod_options == "Device Camera_with_OD_Tracking":
                    #     pass
                    # elif prod_options == "Device Camera_with_Saving_To_Cloud":
                    #     pass

                    # elif prod_options == "Only Streaming":
                    #     # print("This is streaming only")
                    #     st.write("Please Enter the IP Addresses")
                    #     only_streaming(username)

                    # elif prod_options == "Streaming with OD":
                    #     # print("This is object detection")
                    #     st.write("Object Detection")
                    #     streaming_od(username)

                    # elif prod_options == "offline video creation and saving":
                    #     # print("This is for S3 storage only")
                    #     st.write("streaming with s3 storage ")
                    #     form_Streaming_cloud_storage(username, path)

                    # elif prod_options == "Streaming with OD and cloud storage":
                    #     # print("This is for S3 storage only")
                    #     st.write("streaming with s3 storage ")

                    # elif prod_options == "Streaming With OD and Tracking":
                    #     mymain()