import pandas as pd
import streamlit as st
import snowflake.connector as sfc
from datetime import date


sidebar =st.sidebar

whith sidebar:
        account=st.text_input("account")
        username=st.text_input("username")
        password=st.text_input("password",type="password")