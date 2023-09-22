from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="GamingXero", page_icon="👾", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/25e669fa-fd7d-41df-a077-982c59edb63d/6300iI4Dbn.json")
img_snake = Image.open("images/snakeio.png")
img_slide = Image.open("images/spaceslide.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello Gamers, My name is Jaeden :wave:")
    st.title("A Video Game Developer From Caroline County")
    st.write("I make free to play games with awesome in-game content to make your gaming experience more enjoyable")

    # ---- EXAMPLE OF LINK ----
    # ---- st.write("[Learn More >](https://google.com)") ----

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I develop and code games using many python. For those who are looking for:
            - Fighting Games
            - IO Games
            - Puzzle Games
            - Slider Games
            - Dungeon Games

            If this sounds interesting to you, consider trying out some of the games I made.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=375, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_slide)
    with text_column:
        st.subheader("Play this slider game for FREE!")
        st.write(
            """
            Learn how to use the keyboard controls.
            See how long you can survive.
            Most Important, Have FUN!!
            """
        )
        st.markdown("[See the code here!](https://github.com/xerojae/PyGames_Website/blob/master/SliderGame.py)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_snake)
    with text_column:
        st.subheader("Play this IO game for FREE!")
        st.write(
            """
            Learn how to use the keyboard controls. 
            See how much food you can eat.
            Most Important, HAVE FUN!!
            """
        )
        st.markdown("[See the code here!](https://github.com/xerojae/PyGames_Website/blob/master/Snake.py)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/warnercollege1@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name ="message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()