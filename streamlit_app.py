
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default interface to keep the portfolio immersive.
st.markdown(
    """
    <style>
    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    .stApp {
        background: #f5eeea;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "frontend.html"

if not html_path.exists():
    st.error(
        "frontend.html was not found. "
        "Upload it to the same GitHub directory as streamlit_app.py."
    )
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

components.html(
    html_content,
    height=12000,
    scrolling=True,
)
