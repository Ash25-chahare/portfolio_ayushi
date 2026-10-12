
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ayushi Chahare | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_file = Path(__file__).parent / "frontend.html"

if not html_file.exists():
    st.error("frontend.html is missing from the repository.")
    st.stop()

html = html_file.read_text(encoding="utf-8")

# Remove Markdown fences accidentally copied into the HTML file.
html = html.strip()
if html.startswith("```html"):
    html = html[len("```html"):].lstrip()
elif html.startswith("```"):
    html = html[3:].lstrip()

if html.endswith("```"):
    html = html[:-3].rstrip()

# Ensure page content remains visible even if scroll animations fail.
fallback_css = """
<style>
html, body {
    margin: 0 !important;
    padding: 0 !important;
    min-height: 100% !important;
    overflow-x: hidden !important;
}
main, main section, main section .wrap,
main section .reveal, main section .is-visible,
main section .section-head, main section .card,
main section .panel, main section .timeline-item,
main section .skill, main section .profile-card,
main section .wip-feature {
    opacity: 1 !important;
    visibility: visible !important;
    filter: none !important;
}
</style>
"""

if "</head>" in html.lower():
    pos = html.lower().find("</head>")
    html = html[:pos] + fallback_css + html[pos:]
else:
    html = fallback_css + html

components.html(
    html,
    height=14000,
    scrolling=True,
)
