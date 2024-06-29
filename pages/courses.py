import streamlit as st

from db import db_course

st.title('Courses')


@st.experimental_dialog('Add New Course')
def add_new_course():
    new_course = st.text_input('Course Name')
    if st.button('Submit'):
        fetch_response = db_course.fetch({'course': new_course})
        if fetch_response.count == 0:
            db_course.put({'course': new_course})
            st.rerun()


def get_courses_list():
    fetch_response = db_course.fetch()
    if fetch_response.count == 0:
        return []
    courses = [item['course'] for item in fetch_response.items]
    return courses


if st.button('Add New Course'):
    add_new_course()

if any(get_courses_list()):
    for course in get_courses_list():
        col1, col2 = st.columns(2)
        with col1:
            st.write(course)
        with col2:
            if st.button('Delete', key=course):
                res = db_course.fetch({'course': course})
                db_course.delete(res.items[0]['key'])
                st.rerun()
else:
    st.warning("Empty Course Data")


