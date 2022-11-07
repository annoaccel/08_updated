import streamlit as st
from PIL import Image
import numpy as np

import os
from google.cloud import storage

from main import login_user

images = []


# username = login_user.username

img_file_buffer = st.camera_input("Take a picture_centre")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img1 = Image.open(img_file_buffer)
    
    
    st.write("Centre Picture")
    # st.image(img)

    filename1 = str(username) +"_" + "Centre" +".jpg"

    kk1 = img1.save(filename1)
    images.append(filename1)

#--------------------

img_file_buffer2 = st.camera_input("Take a picture_right")

if img_file_buffer2 is not None:
    # To read image file buffer as a PIL Image:
    img2 = Image.open(img_file_buffer2)
    
    st.write("Right Picture")
  

    filename2 = str(username) + "_" + "right" +".jpg"
    images.append(filename2)
    kk2 = img2.save(filename2)

#----------------------

img_file_buffer3 = st.camera_input("Take a picture_left")

if img_file_buffer3 is not None:
    
    img3 = Image.open(img_file_buffer3)
   
    st.write("Left Picture")
   
    filename3 = str(username) + "_ " + "left" +".jpg"
    images.append(filename3)
    kk3 = img3.save(filename3)


try:
    pp1 = Image.open(images[0])
    pp2 = Image.open(images[1])
    pp3 = Image.open(images[2])

    col1, col2, col3 = st.columns(3)

    col1.header("centre")
    col2.header("right")
    col3.header("left")

    col1.image(pp1, use_column_width=True)
    col2.image(pp2, use_column_width=True)
    col3.image(pp3, use_column_width=True)

except:
    print("images not taken")


project_id = "esoteric-parity-366906"
bucket_name = 'avicams' 
# bucket_file = filename
# local_file = filename

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= './esoteric-parity-366906-ebc6bc553872.json'

client = storage.Client(project_id)

bucket = client.get_bucket(bucket_name)


for img in images:
    local_file = img
    bucket_file = img
    blob = bucket.blob(bucket_file)
    blob.upload_from_filename(local_file)


    






    

    
