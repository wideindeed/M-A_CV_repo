import streamlit as st

# Configure the root layout immediately on launch
st.set_page_config(page_title="BUiD CS Portfolios", page_icon="💻", layout="centered")

# Inject a strict global CSS overwrite to hide all distracting sidebar panels and margins
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
        iframe { border-radius: 8px; border: 1px solid #30363d !important; }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# PAGE 1: MAHMOOD MUWAFI
# ─────────────────────────────────────────
def render_mahmood():
    st.subheader("Mahmood Muwafi — Portfolio")
    
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
    
    # FIX: Boost height to 1800 so the entire site renders without an inner scroll track
    st.components.v1.html(html_content, height=1800, scrolling=False)

# ─────────────────────────────────────────
# PAGE 2: AFZAL M. HARISH
# ─────────────────────────────────────────
def render_afzal():
    st.subheader("Afzal M. Harish — Portfolio")
    
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
        
    # FIX: Boost height here as well to cleanly fit his layout matrix
    st.components.v1.html(html_content, height=1800, scrolling=False)

# ─────────────────────────────────────────
# THE MULTIPAGE ROUTING ENGINE
# ─────────────────────────────────────────
page_mahmood = st.Page(render_mahmood, title="Mahmood Muwafi", url_path="mahmood")
page_afzal = st.Page(render_afzal, title="Afzal M. Harish", url_path="friend")

# Lock down navigation execution via clean endpoints hidden from the side layout panels
pg = st.navigation([page_mahmood, page_afzal], position="hidden")
pg.run()