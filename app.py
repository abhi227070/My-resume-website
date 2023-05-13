import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

#This is the page configuration
st.set_page_config(page_title="My resume website",page_icon=":wave:",layout="wide")



def lottie_url(url):

    r=requests.get(url)

    if r.status_code != 200:
        return None
    return r.json()

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

lottie_code=lottie_url("https://assets10.lottiefiles.com/packages/lf20_iv4dsx3q.json")
lottie1_code=lottie_url("https://assets2.lottiefiles.com/private_files/lf30_wyrwqyr9.json")
movie_image=Image.open("machine-learning-project-movie-recommendation-system.webp")
multi_image=Image.open("Heart_Disease_Prediction_using_Machine_Learning.webp")

#Header Section
with st.container():
    st.subheader("Hi I am Abhijeet.")
    st.title("I am an AI developer and a data scientist.")
    st.write('''I am an experienced AI/ML programmer with one year of
    hands-on experience in designing and implementing various
    machine learning models and algorithms. I have a strong
    background in project management and team collaboration,
    which has enabled me to successfully deliver multiple
    projects on time and within budget. My skills in Python
    programming and data analytics, coupled with my ability to
    quickly grasp complex concepts, make me a valuable addition
    to any team looking to leverage AI and ML technologies to
    drive business success.
    ''')

#Certification and animation
with st.container():
    st.write("---")
    st.title("CERTIFICATIONS:")
    left_column,right_column=st.columns(2)
    with left_column:

        st.write('''
        •	Artificial Intelligence and Machine Learning, DevSlope.com(Alison),April 2022.
        
        •	Deep Learning, Deeplearning.ai (Coursera), Feb 2023.
        
        •	Python Programming, Great Learning, Jan 2022.
        
        •	Python programming for Machine Learning, Great Learning, Feb 2023.
        
        •	Project Management, Google (Coursera), April 2023.
        
        •	Entrepreneurship, Startup India Upgrade, Jun 2022.
        
        •	Time Management, Udemy, March 2023.
        ''')

    with right_column:
        st_lottie(lottie_code, height=350, key="code")
#projects
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_side,text_side=st.columns((1,2))

    with image_side:
        st.image(movie_image)
    with text_side:
        st.subheader("Movie Recommendation System:")
        st.write("""
        • Description: A real-time system that recommends movies based
        on users' previous selections. This type of system is used by
        companies like Netflix and YouTube.
        
        • Technologies used: Machine Learning, Deep Learning, NLP, Keras,
        TensorFlow""")
        st.write("[Vist project >](https://abhi227070-movie-recommendation-app-kh1xr6.streamlit.app/)")
    image_side, text_side = st.columns((1, 2))

    with image_side:
        st.image(multi_image)
    with text_side:
        st.subheader("Multiple Disease Prediction:")
        st.write("""
            • Description: A healthcare project that predicts the diseases
            patients suffer from based on data from different machines
            connected to the patient. The system has an accuracy rate of
            95% and is designed to achieve 99% accuracy.

            • Technologies used: Machine Learning, Deep Learning, Keras,
            TensorFlow""")
        st.write("[Vist project >](https://multiple-disease-abhijeet.onrender.com/)")

with st.container():
    st.write("---")
    st.subheader("Get in contect with me")
    st.write("##")

    contact_form="""<form action="https://formsubmit.co/abhijeetmaharana77@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your e-mail" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
    </form>"""

    left_column,right_column=st.columns(2)

    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie1_code,height=300,key="thanks")


