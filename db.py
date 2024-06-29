import deta
import streamlit as st


deta_obj = deta.Deta(st.secrets['DATA_KEY'])
db_student = deta_obj.Base("student")
db_course = deta_obj.Base("course")
db_submission = deta_obj.Base("submission")

