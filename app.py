import streamlit as st
import os

# Set page configuration
st.set_page_config(layout="wide", page_title="G-Take Dashboard")

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Define paths to static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_DIR = os.path.join(BASE_DIR, 'g-take-dashboard')
HTML_PATH = os.path.join(DASHBOARD_DIR, 'index.html')
CSS_PATH = os.path.join(DASHBOARD_DIR, 'styles.css')

# Load content
try:
    html_content = load_file(HTML_PATH)
    css_content = load_file(CSS_PATH)

    # Inject CSS into HTML
    # We replace the link tag or just append the style block into the head or body
    # Since index.html has <link rel="stylesheet" href="styles.css">, we can verify if we want to replace it or just let the iframe handle it if we serve static.
    # However, st.components.v1.html creates an iframe. Relative links inside the iframe might struggle if not served via a web server.
    # Best approach: Embed the CSS directly into the HTML string before rendering.
    
    full_html = f"""
    <style>
    {css_content}
    </style>
    {html_content}
    """
    
    # Render with Streamlit Components
    import streamlit.components.v1 as components
    
    # Adjust height as needed, user requested 1000px
    components.html(full_html, height=1000, scrolling=True)

except FileNotFoundError as e:
    st.error(f"Error loading files: {e}")
    st.info(f"Looking in: {DASHBOARD_DIR}")
