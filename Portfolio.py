import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import cv2
import pandas as pd

def justify_text(text):
    return f'<p style="text-align: justify;">{text}</p>'

st.set_page_config(layout="wide")

selected=option_menu('',['Home','Projects','Contact'],icons=['house','book','envelope'], default_index=0,orientation="horizontal")

if selected =='Home':

    st.write("<div style='text-align:left; color:grey; font-size:50px;'>MY PROFESSIONAL PORTFOLIO</div>", unsafe_allow_html=True)
    img = cv2.imread("photo.png")
    st.image(img,use_column_width=True)
       
    content = """Hi, I am Chirag Radhakrishna. Welcome to my portfolio!!! """
    
    st.write(
        """
        <style>
            .circle {
                width: 15px;
                height: 15px;
                border-radius: 50%;
                display: inline-block;
                margin: 0 10px;
            }
            #circle-1 {
                background-color:  #FF0000;
            }
            #circle-2 {
                background-color: #808080;
            }
            #circle-3 {
                background-color:#008000;
            }
            .circle-container {
                display: flex;
                align-items: center;
                justify-content: center;
                margin-top: 50px;
            }
        </style>
        <div class="circle-container">
            <div class="circle" id="circle-1"></div>
            <div class="circle" id="circle-2"></div>
            <div class="circle" id="circle-3"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.info(content)
    st.write("\n")
    content1  =""" I have worked on projects in several domains inlcuding mobile application development, artificial intelligence, cyber security, machine learning, data visualization
                    and web development. Relevant coursework in data structues, algorithms and object-oriented programming has helped me strengthen my fundamentals. My research interests include: Simulating game-play using Computer Vision and 
                            early disease detection using AI & ML.
                    """
    justified_text = justify_text(content1)                
    st.markdown(justified_text, unsafe_allow_html=True)
    st.write(
        """
        <style>
            .circle {
                width: 15px;
                height: 15px;
                border-radius: 50%;
                display: inline-block;
                margin: 0 10px;
            }
            #circle-1 {
                background-color:  #FF0000;
            }
            #circle-2 {
                background-color: #808080;
            }
            #circle-3 {
                background-color:#008000;
            }
            .circle-container {
                display: flex;
                align-items: center;
                justify-content: center;
                margin-top: 50px;
            }
        </style>
        <div class="circle-container">
            <div class="circle" id="circle-1"></div>
            <div class="circle" id="circle-2"></div>
            <div class="circle" id="circle-3"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    code1 = """
    RECENT UPDATES-
    
    I was awarded the first prize in the paper presentation event for my paper titled 'Multiple Disease Prediction System' at the 18th Karnataka ISTE State 
    Level Student Convention.
    """
     
    st.write("\n")
    st.warning(code1,icon= "🔥")
    st.write("\n")
    
if selected =='Projects':

    st.title('MY PROJECTS')  
    
    df = pd.read_csv("data.csv",sep=";")  
    
    for index, rows in df.iterrows():
            st.header(rows["title"])
            st.write(rows["description"])
            img = cv2.imread(rows["image"])
            st.image(img, use_column_width=True)
            st.write(f"[View Project]({rows['url']})")
            
if selected =='Contact':
    
    st.header("Contact Me")
    
    st.subheader("Reach out on LinkedIn:")
    st.markdown("""
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="chirag-radhakrishna-820a06251" data-version="v1">
            <a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/chirag-radhakrishna-820a06251?trk=profile-badge">CHIRAG RADHAKRISHNA</a>
        </div>
    """, unsafe_allow_html=True)



    
    
            
   
            
