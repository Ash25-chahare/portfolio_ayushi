
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_file = Path(__file__).parent / "index.html"

if not html_file.exists():
    st.error("Portfolio file not found: index.html")
    st.stop()

html_content = html_file.read_text(encoding="utf-8")

st.markdown(
    """
    <style>
        #MainMenu, footer, header,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"] {
            display: none !important;
        }

        .stApp, [data-testid="stAppViewContainer"],
        [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    html_content,
    height=10000,
    scrolling=True,
)
