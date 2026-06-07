import streamlit as st

# Configure the root layout immediately on launch
st.set_page_config(page_title="BUiD CS Portfolios", page_icon="💻", layout="wide")

# Inject "App Mode" CSS: This kills the double scrollbar and forces fullscreen
st.markdown("""
    <style>
        /* Hide all Streamlit headers and menus */
        [data-testid="stHeader"] { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        
        /* Remove padding and lock the outer background from scrolling */
        .block-container { 
            padding: 1rem 0 0 0 !important; 
            max-width: 100% !important; 
            overflow: hidden !important;
        }
        
        /* Force the iframe to fill the screen natively */
        iframe { 
            border: none !important; 
            border-radius: 0 !important; 
            width: 100% !important; 
            height: 88vh !important; /* Leaves perfect space for the download button */
        }
        
        /* Style the download button container to look like a clean top-bar */
        [data-testid="stElementContainer"]:has([data-testid="stDownloadButton"]) {
            padding: 0 1rem;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# PAGE 1: MAHMOOD MUWAFI
# ─────────────────────────────────────────
def render_mahmood():
    # Removed the st.subheader to avoid double-titles!
    
    with open("Resume2026.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Mahmood's CV (PDF)",
            data=pdf_file.read(),
            file_name="Mahmood_Muwafi_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Re-enabled scrolling and removed fixed height so the CSS takes over
    st.components.v1.html(html_content, scrolling=True)

# ─────────────────────────────────────────
# PAGE 2: AFZAL M. HARISH
# ─────────────────────────────────────────
def render_afzal():
    # Removed the st.subheader here too!
    
    with open("Job Resume-1.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Afzal's CV (PDF)",
            data=pdf_file.read(),
            file_name="Afzal_M_Harish_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    with open("index_af.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # Re-enabled scrolling
    st.components.v1.html(html_content, scrolling=True)

# ─────────────────────────────────────────
# THE MULTIPAGE ROUTING ENGINE
# ─────────────────────────────────────────
page_mahmood = st.Page(render_mahmood, title="Mahmood Muwafi", url_path="mahmood")
page_afzal = st.Page(render_afzal, title="Afzal M. Harish", url_path="friend")

pg = st.navigation([page_mahmood, page_afzal], position="hidden")

# Homepage Fallback
if "page" not in st.query_params:
    st.query_params["page"] = "mahmood"

pg.run()