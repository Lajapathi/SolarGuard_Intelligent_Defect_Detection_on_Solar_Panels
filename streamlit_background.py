import streamlit as st
import base64


@st.cache_data
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_full_background(image_path):
    img_data = get_base64(image_path)
    st.markdown(f"""
        <style>
        html, body {{
            margin: 0; padding: 0; height: 100%; background: transparent;
        }}

        /* Main app wrapper */
        .stApp {{
            background-color: transparent !important;
            background-image: url("data:image/png;base64,{img_data}");
            background-size: cover;!important;
            background-position: center;!important;
            background-repeat: no-repeat;!important;
            background-attachment: fixed;!important;
            height: 100vh;
        }}

        /* Sidebar including all nested containers */
        [data-testid="stSidebar"] {{
            background-color: transparent !important;
            background-image: url("data:image/png;base64,{img_data}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
            /* background-color: transparent !important; */
            
        }}

        [data-testid="stSidebar"] * {{
            /* background-color: transparent !important; */
            
        }}

        /* Top header */
        header, [data-testid="stToolbar"] {{
            background-color: transparent !important;
            background-image: url("data:image/png;base64,{img_data}");
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
            background: transparent !important;
        }}

        /* Main content container */
        [data-testid="stAppViewContainer"] > main {{
            background: transparent !important;
        }}

        .block-container {{
            padding-top: 1rem !important;
        }}
        </style>
    """, unsafe_allow_html=True)