import streamlit as st
import pandas as pd

st.set_page_config(page_title="Brodix Fan Compass - LALIGA", layout="wide")

st.markdown("## 🧭 Brodix Fan Compass | LALIGA Belonging OS v2.4.1")
st.divider()

left, center, right = st.columns([1,1.5,1])

with left:
    st.markdown("### 🛡️ FAN TRUTHRANK")
    st.image("https://i.pravatar.cc/150?img=12", width=100)
    st.write("**Diego Martinez**")
    st.caption("Verified Fan Tier 3")
    st.metric("TruthRank", "92/100", "+3")
    st.metric("Authenticity", "94%")
    st.success("Belonging Streak: 14 days")

with center:
    st.markdown("### ⚽ LIVE MATCH")
    st.markdown("🔴 LIVE - Real Madrid VS Barcelona")
    st.write("Real Madrid Win - 47%")
    st.progress(47)
    st.write("Draw - 22%")
    st.progress(22)
    st.write("Barcelona Win - 31%")
    st.progress(31)
    pred = st.radio("YOUR PREDICTION:", ["Real Madrid Win", "Draw", "Barcelona Win"], horizontal=True)
    if st.button("Submit Prediction +25 BP", type="primary"):
        st.balloons()
        st.success(f"Submitted {pred} +25 BP!")

with right:
    st.markdown("### 🏆 LEADERBOARD")
    df = pd.DataFrame([{"Rank":"#1","Name":"Laia_RM1902","BP":"12,840"},{"Rank":"#2","Name":"BarcaFan_88","BP":"11,201"},{"Rank":"#5","Name":"You","BP":"7,540"}])
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.metric("Your Rank", "#5 / 12,409")

st.divider()
st.caption("Ignyte x LALIGA Beyond The Match | $10,000 | Demo Nov 02, 2026")
