import streamlit as st

st.set_page_config(
    page_title="Portfolio | arief mohamad",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SUGENG RAWUH DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 390)

with col2:
   st.header("Data Diri")
   st.subheader("NAMA : MOHAMAD ARIEF FAKHRUDIN Z")
   st.caption("NIM : 0402201102")
   st.write(
            """
            - Tempat Tanggal Lahir :Brebes 16 April 2002 
            - Alamat :Kecipir Losari Brebes
            - Hobi : Game
            - Cita-cita : Jadi Orang Manfaat
            - Hal yang disukai : Eat
            - Status : Sudah Di Miliki
            """
        )
col1, col2, col3, col4, = st.columns(4)
with col1:
   
    st.image("yt.png", width= 50)
    st.link_button("Youtube Chanel", "http://www.youtube.com/@berkahngabdi2171")
with col2:
   
    st.image("fb.png", width= 50)
    st.link_button("Facebook", "https://www.facebook.com/jonibrada.olengvsetitik?mibextid=rS40aB7S9Ucbxw6v")
with col3:
    
    st.image("ig.png", width= 50)
    st.link_button("Instagram", "https://instagram.com/kang_rokhman?igshid=YTQwZjQ0NmI0OA%3D%3D")
with col4:
    
    st.image("x.png", width= 50)
    st.link_button("TikTok", "tuwitter", "https://twitter.com/faisalrokhman4")


st.header("*Call Me If You Want*")

st.link_button("Go to contact", "http://localhost:8501/contact")
