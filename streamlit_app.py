
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Read the actual HTML file in the repository.
BASE_DIR = Path(__file__).parent
html_file = BASE_DIR / "index.html"

if not html_file.exists():
    st.error("index.html was not found.")
    st.write("Files in repository:", [p.name for p in BASE_DIR.iterdir()])
    st.stop()

html = html_file.read_text(encoding="utf-8")

# Remove accidental Markdown fences.
html = html.strip()
if html.startswith("```html"):
    html = html[len("```html"):].lstrip()
elif html.startswith("```"):
    html = html[3:].lstrip()

if html.endswith("```"):
    html = html[:-3].rstrip()

# Force the animated content to remain visible.
fix_css = """
<style>
.reveal {
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
    filter: none !important;
}
#intro {
    display: none !important;
}
</style>
"""

html = html.replace("</head>", fix_css + "</head>", 1)

components.html(
    html,
    height=14000,
    scrolling=True,
)
