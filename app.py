import streamlit as st

# Configure the root layout immediately on launch
st.set_page_config(page_title="BUiD CS Portfolios", page_icon="💻", layout="wide")

# Inject "App Mode" CSS
st.markdown("""
    <style>
        [data-testid="stHeader"] { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        .block-container { 
            padding: 1rem 0 0 0 !important; 
            max-width: 100% !important; 
            overflow: hidden !important;
        }
        iframe { 
            border: none !important; 
            border-radius: 0 !important; 
            width: 100% !important; 
            height: 88vh !important; 
        }
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
    with open("Resume2026.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Mahmood's CV (PDF)",
            data=pdf_file.read(),
            file_name="Mahmood_Muwafi_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    # 1. Read all three of your files
    with open("index.html", "r", encoding="utf-8") as f: html = f.read()
    with open("style.css", "r", encoding="utf-8") as f: css = f.read()
    with open("main.js", "r", encoding="utf-8") as f: js = f.read()
    
    # 2. Stitch the CSS and JS directly into the HTML string
    html = html.replace("</head>", f"<style>{css}</style></head>")
    html = html.replace("</body>", f"<script>{js}</script></body>")
    
    # 3. Render the fully combined site
    st.components.v1.html(html, height=2500, scrolling=True)

# ─────────────────────────────────────────
# PAGE 2: AFZAL M. HARISH
# ─────────────────────────────────────────
def render_afzal():
    with open("Job Resume-1.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Afzal's CV (PDF)",
            data=pdf_file.read(),
            file_name="Afzal_M_Harish_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    # 1. Read all three of his files
    with open("index_af.html", "r", encoding="utf-8") as f: html = f.read()
    with open("style_af.css", "r", encoding="utf-8") as f: css = f.read()
    with open("main_af.js", "r", encoding="utf-8") as f: js = f.read()
    
    # 2. Stitch the CSS and JS directly into the HTML string
    html = html.replace("</head>", f"<style>{css}</style></head>")
    html = html.replace("</body>", f"<script>{js}</script></body>")
        
    # 3. Render the fully combined site
    st.components.v1.html(html, height=2500, scrolling=True)

# ─────────────────────────────────────────
# THE MULTIPAGE ROUTING ENGINE
# ─────────────────────────────────────────

# 1. Define the pages clearly
# Note: We remove the url_path from your default page so it cleanly matches the root domain
page_mahmood = st.Page(render_mahmood, title="Mahmood Muwafi", default=True)
page_afzal = st.Page(render_afzal, title="Afzal M. Harish", url_path="friend")

# 2. Initialize the navigation control structure
pg = st.navigation([page_mahmood, page_afzal], position="hidden")

# 3. Check if someone is specifically trying to look for your old path name
if "page" in st.query_params and st.query_params["page"] == "mahmood":
    # Clear the query param and let the default dashboard route take over natively
    st.query_params.clear()

# 4. Run the navigation layout engine
pg.run()