     import streamlit as st
import pandas as pd
from datetime import date

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
    --bg: #080b12; --line: #283244; --text: #f3f5fb; --muted: #9aa7ba;
}
.stApp {
    background: radial-gradient(ellipse at 15% 0%, #182442 0%, transparent 35%), var(--bg);
    color: var(--text); font-family: 'Inter', sans-serif;
}
.block-container { max-width: 1450px; padding-top: 1.5rem; }
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #151e2c, #101620);
    border: 1px solid var(--line); padding: 18px; border-radius: 16px; min-height: 115px;
}
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg, #141c29, #0f151f);
    border: 1px solid var(--line); border-radius: 18px; padding: 15px;
}
.stButton > button {
    background: linear-gradient(100deg, #ff5264, #ef344e);
    color: white; border: 0; border-radius: 10px; min-height: 43px; font-weight: 800;
}
.small-label { color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; font-size: 10px; font-weight: 800; }
.live { display: inline-block; background: #3a1722; color: #ff7486; padding: 6px 10px; border: 1px solid #6b2637; border-radius: 20px; font-size: 11px; font-weight: 800; }
.hero { padding: 23px; border: 1px solid #303c53; border-radius: 20px; background: radial-gradient(circle at 90% 10%, #26375a 0%, transparent 38%), linear-gradient(120deg, #151f31, #10151f); margin-bottom: 18px; }
.hero-sub { color: #a9b6ca; font-size: 13px; line-height: 1.7; }
.club { background: #0d1420; border: 1px solid #293548; border-radius: 14px; padding: 15px 8px; text-align: center; }
.footer { color: #738198; text-align: center; font-size: 11px; padding: 20px 0; }
.avatar-wrap { text-align:center; }
.avatar-wrap img { width:120px; height:120px; border-radius:50%; border:3px solid #39dba0; object-fit:cover; box-shadow:0 0 25px #39dba050; }
</style>
""", unsafe_allow_html=True)

# HEADER
header_left, header_right = st.columns([3, 1])
with header_left:
    st.markdown("<div class='small-label'>FAN IDENTITY · MATCH INTELLIGENCE</div>", unsafe_allow_html=True)
    st.title("🧭 Brodix Fan Compass")
    st.caption("LALIGA Belonging OS · v2.5")
with header_right:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:right'><span class='live'>● DEMO MATCH</span></div>", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="small-label">YOUR FAN JOURNEY</div>
  <h2 style="margin:8px 0">More than a match.<br><span style="color:#ff6477">You belong here.</span></h2>
  <div class="hero-sub">Track your fan identity, make match predictions, earn Belonging Points and climb the community leaderboard.</div>
</div>
""", unsafe_allow_html=True)

# FAN PROFILE - WITH YOUR FACE
st.markdown("### 🛡️ Fan TruthRank")
profile_col, stats_col = st.columns([1, 2])

with profile_col:
    with st.container(border=True):
        # DITO NA MUKHA MO BOSS - HINDI NA 👤
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image("avatar.jpg", use_container_width=True) # <-- LAGAY MO YUNG SELFIE MO AS avatar.jpg

        st.markdown("<div style='text-align:center;font-weight:900;font-size:19px;margin-top:10px'>Brodix Fan</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align:center;color:#9aa7ba;font-size:12px'>Verified Fan · Tier 3 ✅</div>", unsafe_allow_html=True)
        st.divider()
        st.metric("TruthRank", "92/100", "+3")
        st.metric("Authenticity", "94%")
        st.markdown(f"<div style='background:#123a30;color:#49e0ae;padding:12px;border-radius:10px;text-align:center;font-weight:800;border:1px solid #39dba030'>🔥 {st.session_state.streak}-Day Belonging Streak</div>", unsafe_allow_html=True)

with stats_col:
    with st.container(border=True):
        st.markdown("#### Your fan impact")
        st.caption("Your demo profile at a glance.")
        a, b = st.columns(2)
        a.metric("Belonging Points", f"{st.session_state.bp:,}")
        b.metric("Community Rank", "#5", "Demo ranking")
        st.markdown("**Fan participation level**")
        st.progress(0.92)
        st.caption("92% · Illustrative TruthRank score")
        st.markdown("**Community contribution**")
        st.progress(min(st.session_state.bp / 10000, 1.0))
        st.caption("Progress toward 10,000 BP")

# LIVE MATCH
st.markdown("---")
st.markdown("### ⚽ Match Center")
match_left, match_right = st.columns([1.35, 1])
with match_left:
    with st.container(border=True):
        st.markdown("<span class='live'>● SIMULATED MATCH</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        team1, versus, team2 = st.columns([2, 1, 2])
        with team1:
            st.markdown("<div class='club'><div style='font-size:35px'>⚪</div><div style='font-size:12px;font-weight:800'>REAL MADRID</div></div>", unsafe_allow_html=True)
        with versus:
            st.markdown("<div style='text-align:center;padding-top:24px;font-size:18px;font-weight:900;color:#9aa7ba'>VS</div>", unsafe_allow_html=True)
        with team2:
            st.markdown("<div class='club'><div style='font-size:35px'>🔵🔴</div><div style='font-size:12px;font-weight:800'>BARCELONA</div></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        for label, value in [("Real Madrid Win", 47), ("Draw", 22), ("Barcelona Win", 31)]:
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"**{label}**")
            c2.markdown(f"<div style='text-align:right;font-weight:900'>{value}%</div>", unsafe_allow_html=True)
            st.progress(value / 100)

with match_right:
    with st.container(border=True):
        st.markdown("#### 🎯 Your Prediction")
        choice = st.radio("Match outcome", ["Real Madrid Win", "Draw", "Barcelona Win"], index=["Real Madrid Win", "Draw", "Barcelona Win"].index(st.session_state.prediction), key="prediction_radio")
        if st.button("Submit Prediction · +25 BP", use_container_width=True):
            if not st.session_state.submitted:
                st.session_state.prediction = choice
                st.session_state.bp += 25
                st.session_state.submitted = True
                st.success("Prediction recorded! 25 demo BP awarded.")
                st.rerun()
            else:
                st.info("You have already submitted a prediction for this demo match.")
        if st.session_state.submitted:
            st.success(f"Your pick: {st.session_state.prediction}")

# LEADERBOARD
st.markdown("---")
st.markdown("### 🏆 Community Leaderboard")
leaderboard = pd.DataFrame([
    {"Rank": 1, "Fan": "LaLiga_RM1907", "BP": 17840},
    {"Rank": 2, "Fan": "BarcaFan_88", "BP": 11201},
    {"Rank": 3, "Fan": "FootballSoul", "BP": 9840},
    {"Rank": 4, "Fan": "MatchDayPro", "BP": 8260},
    {"Rank": 5, "Fan": "You", "BP": st.session_state.bp},
])
leaderboard = leaderboard.sort_values("BP", ascending=False).reset_index(drop=True)
leaderboard["Rank"] = range(1, len(leaderboard) + 1)
left, right = st.columns([1.5, 1])
with left:
    st.dataframe(leaderboard, hide_index=True, use_container_width=True)
with right:
    your_rank = int(leaderboard.index[leaderboard["Fan"] == "You"][0]) + 1
    st.metric("Current Demo Rank", f"#{your_rank}")
    st.metric("Your BP", f"{st.session_state.bp:,}")

st.markdown("<div class='footer'>BRODIX FAN COMPASS · LALIGA BELONGING OS · INNOVATION DEMO</div>", unsafe_allow_html=True)     
