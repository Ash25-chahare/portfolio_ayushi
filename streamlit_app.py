from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "index.html"

st.markdown(
    """
    <style>
        #MainMenu, footer, header,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"] {
            display: none !important;
        }

        html, body, .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {
            background: #f5eeea !important;
        }

        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        iframe {
            display: block;
            border: none !important;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.exists():
    st.error("The file index.html is missing.")
    st.write("Files currently available:", [p.name for p in BASE_DIR.iterdir()])
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

if not html.strip():
    st.error("index.html is empty.")
    st.stop()

if "<html" not in html.lower() or "<body" not in html.lower():
    st.error("index.html must contain a complete HTML document.")
    st.stop()

# Load the HTML portfolio directly inside the Streamlit page.
components.html(
    html,
    height=12000,
    scrolling=True,
)
