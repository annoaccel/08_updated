import streamlit as st
import os
# from dotenv import load_dotenv
import streamlit_google_oauth as oauth
# from options import *
# load_dotenv()
# client_id = os.environ["GOOGLE_CLIENT_ID"]
# client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
# redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]


login_info = oauth.login(
    client_id='825136727091-4kdt4v8pl9rcu7ajshf29caebc79uci8.apps.googleusercontent.com',
    client_secret='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',
    redirect_uri="http://localhost:8080",
    login_button_text="Continue with Google",
    logout_button_text="Logout",
)

if login_info:
    user_id, user_email = login_info
    st.write(f"Welcome {user_email}")
    # func_login()
else:
    st.write("Please login")




# client_id = os.environ["GOOGLE_CLIENT_ID"]
# client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
# redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]


# def new_glogin():
#     client_id='825136727091-4kdt4v8pl9rcu7ajshf29caebc79uci8.apps.googleusercontent.com'
#     client_secret='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'
#     redirect_uri= "http://localhost:8080"


#     login_info = oauth.login(
#         client_id=client_id,
#         client_secret=client_secret,
#         redirect_uri=redirect_uri,
#         login_button_text="Continue with Google",
#         logout_button_text="Logout",
#     )
#     if login_info:
#         user_id, user_email = login_info
#         st.write(f"Welcome {user_email}")
#         pass
#         # func_login()
#     else:
#         st.write("Please login")

#     return

