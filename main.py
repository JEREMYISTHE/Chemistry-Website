st.markdown("""
<style>

/* Hide footer (ALL versions) */
footer {display: none !important;}
[data-testid="stFooter"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

/* Sometimes Streamlit wraps it in this */
.css-164nlkn {display: none !important;}

/* Keep menu */
header {visibility: visible !important;}

/* Background */
.stApp {
    background: linear-gradient(to bottom, #0f172a, #111827);
}

/* Text */
h1, h2, h3, p {
    color: white;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 16px;
    border-radius: 10px;
    background-color: black !important;
    color: white !important;
    border: 1px solid white;
}

</style>
""", unsafe_allow_html=True)