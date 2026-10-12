
from pathlib import Path
import re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit's page uncluttered.
st.markdown("""
<style>
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    display: none !important;
}
.stApp, [data-testid="stAppViewContainer"] {
    background: #f5eeea;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

file_path = Path(__file__).parent / "frontend.html"

if not file_path.is_file():
    st.error("Cannot find frontend.html beside streamlit_app.py.")
    st.write("Files found in this folder:")
    st.write([p.name for p in Path(__file__).parent.iterdir()])
    st.stop()

html = file_path.read_text(encoding="utf-8").strip()

# Remove Markdown fences accidentally pasted into the file.
html = re.sub(r"^\s*```(?:html)?\s*", "", html, flags=re.IGNORECASE)
html = re.sub(r"\s*```\s*$", "", html)

if "<html" not in html.lower() or "<body" not in html.lower():
    st.error("frontend.html does not contain a complete HTML document.")
    st.stop()

# Disable entrance effects that can leave content invisible.
emergency_css = """
<style>
html, body {
    min-height: 100% !important;
    height: auto !important;
    overflow-x: hidden !important;
    background: #f5eeea !important;
}
#motion-curtain, #intro, #route-wipe {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}
.reveal, .is-visible, .section-head,
.section-title .word > span,
main, main section, main section *,
section .wrap, .hero, .profile-card,
.project, .wip-card, .resume-card,
.education-card, .panel, .skill,
.timeline-item, .contact-panel {
    visibility: visible !important;
    opacity: 1 !important;
    filter: none !important;
}
.reveal, .section-title .word > span {
    transform: none !important;
    animation: none !important;
}
</style>
"""

# Insert emergency styles inside the existing head.
head_match = re.search(r"</head\s*>", html, flags=re.IGNORECASE)
if head_match:
    html = html[:head_match.start()] + emergency_css + html[head_match.start():]
else:
    html = emergency_css + html

st.caption("Portfolio diagnostic mode")

components.html(
    html,
    height=14000,
    scrolling=True,
)
