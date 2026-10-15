
  import streamlit as st
import pandas as pd

st.set_page_config(page_title="Brodix Fan Compass", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

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
:root{--bg:#080b12;--line:#283244;--text:#f3f5fb;--muted:#9aa7ba}
.stApp{background:radial-gradient(ellipse at 15% 0%,#182442 0%,transparent 35%),var(--bg);color:var(--text);font-family:Inter,sans-serif}
.block-container{max-width:1450px;padding-top:1.5rem}
[data-testid="stMetric"]{background:linear-gradient(145deg,#151e2c,#101620);border:1px solid var(--line);padding:18px;border-radius:16px}
div[data-testid="stVerticalBlockBorderWrapper"]{background:linear-gradient(145deg,#141c29,#0f151f);border:1px solid var(--line);border-radius:18px;padding:15px}
.stButton>button{background:linear-gradient(100deg,#ff5264,#ef344e);color:white;border:0;border-radius:10px;min-height:43px;font-weight:800}
.small-label{color:var(--muted);text-transform:uppercase;letter-spacing:1.5px;font-size:10px;font-weight:800}
.live{display:inline-block;background:#3a1722;color:#ff7486;padding:6px 10px;border:1px solid #6b2637;border-radius:20px;font-size:11px;font-weight:800}
.hero{padding:23px;border:1px solid #303c53;border-radius:20px;background:radial-gradient(circle at 90% 10%,#26375a 0%,transparent 38%),linear-gradient(120deg,#151f31,#10151f);margin-bottom:18px}
.hero-sub{color:#a9b6ca;font-size:13px}
.club{background:#0d1420;border:1px solid #293548;border-radius:14px;padding:15px 8px;text-align:center}
.footer{color:#738198;text-align:center;font-size:11px;padding:20px 0}
</style>
""", unsafe_allow_html=True)

c1,c2=st.columns([3,1])
with c1:
    st.markdown("<div class='small-label'>FAN IDENTITY · MATCH INTELLIGENCE</div>", unsafe_allow_html=True)
    st.title("🧭 Brodix Fan Compass")
    st.caption("LALIGA Belonging OS · v2.5")
with c2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:right'><span class='live'>● DEMO MATCH</span></div>", unsafe_allow_html=True)

st.markdown("""<div class="hero"><div class="small-label">YOUR FAN JOURNEY</div><h2 style="margin:8px 0">More than a match.<br><span style="color:#ff6477">You belong here.</span></h2><div class="hero-sub">Track your fan identity, make match predictions, earn Belonging Points and climb the community leaderboard.</div></div>""", unsafe_allow_html=True)

st.markdown("### 🛡️ Fan TruthRank")
pc, sc = st.columns([1,2])
with pc:
    with st.container(border=True):
        st.markdown("<div style='
