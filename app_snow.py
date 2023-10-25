import pandas as pd
import streamlit as st
import snowflake.connector as sfc
from datetime import date


sidebar =st.sidebar

with sidebar:
        account=st.text_input("account")
        username=st.text_input("username")
        password=st.text_input("password",type="password")
        role=st.text_input("role")
        wh=st.text_input("Warehouse")
        db=st.text_input("database")