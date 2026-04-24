st.markdown("""
<style>

/* Hide EVERYTHING at the bottom */
[data-testid="stFooter"] {
    display: none;
}

/* Hide GitHub icon + "Made with Streamlit" */
[data-testid="stDecoration"] {
    display: none;
}

/* Keep hamburger menu */
header {
    visibility: visible;
}

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