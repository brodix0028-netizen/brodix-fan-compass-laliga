  import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Brodix Fan Compass",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "bp" not in st.session_state:
    st.session_state.bp = 7540
if "prediction" not in st.session_state:
    st.session_state.prediction = "Real Madrid Win"
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "streak" not in st.session_state:
    st.session_state.streak = 14

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root {
    --bg: #080b12;
    --panel: #111722;
    --line: #283244;
    --text: #f3f5fb;
    --muted: #9aa7ba;
}
.stApp {
    background: radial-gradient(ellipse at 15% 0%, #182442 0%, transparent 35%), var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { max-width: 1450px; padding-top: 1.5rem; padding-bottom: 3rem; }
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #151e2c, #101620);
    border: 1px solid var(--line);
    padding: 18px;
    border-radius: 16px;
    min-height: 115px;
}
[data-testid="stMetricLabel"] { color: var(--muted)!important; font-size: 11px!important; }
[data-testid="stMetricValue"] { color: var(--text)!important; font-weight: 800!important; }
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg, #141c29, #0f151f);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 15px;
}
.stButton > button {
    background: linear-gradient(100deg, #ff5264, #ef344e);
    color: white; border: 0; border-radius: 10px; min-height: 43px; font-weight: 800;
}
.stRadio label { color: var(--text)!important; }
.small-label { color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; font-size: 10px; font-weight: 800; }
.live { display: inline-block; background: #3a1722; color: #ff748
