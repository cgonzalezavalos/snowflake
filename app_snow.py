import pandas as pd
import streamlit as st
import snowflake.connector as sf
from datetime import date


sidebar =st.sidebar

def con_to_snow(acc,usr,pwd,rol,war,dbs):
        con=sf.connect(user=usr,account=acc,password=pwd, role=rol,warehouse=war,database=dbs)
        cs=con.cursor()
        return cs


with sidebar:
        account=st.text_input("account")
        username=st.text_input("username")
        password=st.text_input("password",type="password")
        role=st.text_input("role")
        wh=st.text_input("Warehouse")
        db=st.text_input("database")
        connect=st.button("Conectar a Snowflake",\
                          on_click=con_to_snow,\
                            args=(account,username,password,role,wh,db))