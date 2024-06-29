import streamlit as st

from db import db_course, db_student

st.title('Enroll Student')

res = db_course.fetch()
courses = [item['course'] for item in res.items]

with st.form('enroll_student', clear_on_submit=True):
    course = st.selectbox('Course', courses)
    student_id = st.text_area(label='Student ID')

    for student in student_id.split('\n'):
        db_student.put({'student_id': student, 'course': course})

    st.form_submit_button('Submit')
