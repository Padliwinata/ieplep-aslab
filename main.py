import streamlit as st


pg = st.navigation([st.Page('pages/enroll.py', title='Enroll Student'),
                    st.Page('pages/question_bank.py', title='Question Bank'),
                    st.Page('pages/courses.py', title='Courses')])

pg.run()

