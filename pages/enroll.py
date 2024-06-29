import streamlit as st

from db import db_course, db_student

st.title('Enroll Student')

res = db_course.fetch()
courses = [item['course'] for item in res.items]

course = st.selectbox('Course', courses)
student_id = st.text_area(label='Student ID')

for student in student_id.split('\n'):
    db_student.put({'student_id': student, 'course': course})

