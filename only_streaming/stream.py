import streamlit as st
from forms.form_only_streaming import *
from vc.vc_streaming import *

camerascc = only_streaming()
st_multi_window(camerascc)

