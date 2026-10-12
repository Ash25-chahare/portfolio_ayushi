
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
    }
    .stApp, [data-testid="stAppViewContainer"] {
        background: #f5eeea;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        display: block;
        border: 0 !important;
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_file = Path(__file__).parent / "frontend.html"

if not html_file.exists():
    st.error("frontend.html is missing from the repository root.")
    st.stop()

html = html_file.read_text(encoding="utf-8")

# Remove accidental Markdown fences if the file was copied from a code block.
html = html.strip()
if html.startswith("```html"):
    html = html[len("```html"):].lstrip()
elif html.startswith("```"):
    html = html[3:].lstrip()

if html.endswith("```"):
    html = html[:-3].rstrip()

if "<html" not in html.lower() or "<body" not in html.lower():
    st.error("frontend.html does not appear to contain a complete HTML document.")
    st.stop()

components.html(
    html,
    height=14000,
    scrolling=True,
)
