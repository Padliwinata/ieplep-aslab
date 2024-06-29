import os
import streamlit as st

from db import db_course


def generate_file_upload(module: int):
    list_question = []
    for i in range(module):
        list_question.append(st.file_uploader(label=f'Soal Modul {i+1}'))

    return list_question


st.title("Upload Question Bank")

res = db_course.fetch()
courses = [item['course'] for item in res.items]

course = st.selectbox('Course', courses)

module_num = st.number_input(min_value=1, max_value=15, label='Number of Module')
questions = generate_file_upload(module_num)

if st.button('submit'):
    for i in range(module_num):
        filename = f'questions/{course}/MOD{i+1}.pdf'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as file:
            file.write(questions[i].read())
    st.rerun()


