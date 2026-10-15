
import streamlit as st
import pandas as pd
from datetime import datetime

# ==================================================
# BRODIX FAN COMPASS | LALIGA BELONGING OS
# Full Streamlit prototype with profile photo upload
# ==================================================

st.set_page_config(
    page_title="Brodix Fan Compass",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE -------------------

defaults = {
    "bp": 7540,
    "streak": 14,
    "prediction": None,
    "submitted": False,
    "fan_name": "Brodix Fan",
    "fan_tier": "Tier 3",
    "cases": None,
    "activity": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

if st.session_state.cases is None:
    st.session_state.cases = pd.DataFrame([
        {"Fan": "LaLiga_RM1907", "BP": 17840},
        {"Fan": "BarcaFan_88", "BP": 11201},
        {"Fan": "FootballSoul", "BP": 9840},
        {"Fan": "MatchDayPro", "BP": 8260},
        {"Fan": "You", "BP": st.session_state.bp},
    ])

# ---------------- PREMIUM DESIGN ------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg:#080b12;
    --panel:#121a28;
    --line:#29364a;
    --text:#f3f6fc;
    --muted:#9aa9bf;
    --red:#ff5268;
    --green:#42dfb9;
    --blue:#579cff;
    --gold:#ffc969;
}

.stApp {
    background:
      radial-gradient(ellipse at 15% 0%, #182442 0%, transparent 36%),
      var(--bg);
    color:var(--text);
    font-family:'Inter',sans-serif;
}

header[data-testid="stHeader"] {
    background:transparent;
}

.block-container {
    max-width:1400px;
    padding-top:1.5rem;
    padding-bottom:3rem;
}

h1 {
    font-size:clamp(25px,4vw,39px)!important;
    font-weight:900!important;
    letter-spacing:-1.3px;
}

h2,h3 {
    color:var(--text)!important;
    font-weight:800!important;
}

p, label {
    color:var(--text);
}

[data-testid="stMetric"] {
    background:linear-gradient(145deg,#172235,#101620);
    border:1px solid var(--line);
    padding:16px;
    border-radius:15px;
    min-height:105px;
}

[data-testid="stMetricLabel"] {
    color:var(--muted)!important;
    font-size:12px!important;
}

[data-testid="stMetricValue"] {
    color:var(--text)!important;
    font-weight:800!important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:linear-gradient(145deg,#141d2b,#0e141e);
    border:1px solid var(--line);
    border-radius:17px;
    padding:14px;
}

.stButton>button {
    background:linear-gradient(100deg,#ff5268,#ed3653);
    color:white;
    border:0;
    border-radius:10px;
    min-height:42px;
    font-weight:800;
}

.stButton>button:hover {
    color:white;
    border:1px solid #ff8493;
    background:#ff6478;
}

.stProgress > div > div > div > div {
    background:linear-gradient(90deg,#579cff,#42dfb9);
}

hr {
    border-color:var(--line);
}

.eyebrow {
    font-size:10px;
    letter-spacing:2px;
    font-weight:800;
    color:var(--green);
    text-transform:uppercase;
}

.hero {
    padding:24px;
    border:1px solid #303c53;
    border-radius:20px;
    background:
      radial-gradient(circle at 90% 10%,#26375a 0%,transparent 38%),
      linear-gradient(120deg,#151f31,#10151f);
    margin-bottom:18px;
}

.hero p {
    color:var(--muted);
    line-height:1.7;
}

.pill {
    display:inline-block;
    background:#351923;
    color:#ff8392;
    border:1px solid #6b2b3b;
    border-radius:30px;
    padding:6px 10px;
    font-size:11px;
    font-weight:800;
}

.club {
    background:#0b1422;
    border:1px solid var(--line);
    border-radius:14px;
    text-align:center;
    padding:17px 5px;
}

.club-icon {
    font-size:35px;
}

.club-name {
    font-size:11px;
    font-weight:900;
}

.small {
    color:var(--muted);
    font-size:12px;
}

.footer {
    color:#74829a;
    text-align:center;
    font-size:11px;
    padding:22px 0;
}

@media(max-width:640px) {
    .block-container {
        padding-left:11px;
        padding-right:11px;
        padding-top:1rem;
    }

    [data-testid="stMetric"] {
        padding:11px;
        min-height:94px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR -------------------------

with st.sidebar:
    st.markdown("## 🧭 Fan Compass")

    page = st.radio(
        "Navigate",
        [
            "Fan Dashboard",
            "Match Center",
            "Leaderboard",
            "Fan Settings"
        ]
    )

    st.divider()

    st.caption("LALIGA Belonging OS")
    st.caption("Independent prototype · v2.5")

# ---------------- HEADER --------------------------

header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown(
        '<div class="eyebrow">FAN IDENTITY · MATCH INTELLIGENCE</div>',
        unsafe_allow_html=True
    )
    st.title("🧭 Brodix Fan Compass")

with header_right:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:right">'
        '<span class="pill">● DEMO MODE</span></div>',
        unsafe_allow_html=True
    )

st.markdown("""
<div class="hero">
    <div class="eyebrow">YOUR FAN JOURNEY</div>
    <h2 style="margin:9px 0;font-size:clamp(25px,4vw,38px)">
        More than a match.<br>
        <span style="color:#ff6478">You belong here.</span>
    </h2>
    <p>
        Celebrate your football identity, predict match outcomes,
        earn demo Belonging Points, and explore your fan community.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- PROFILE PHOTO -------------------

def render_profile():
    st.markdown("### 🛡️ Fan TruthRank")

    profile_col, stats_col = st.columns([1, 2])

    with profile_col:
        with st.container(border=True):

            st.markdown(
                '<div class="eyebrow" style="text-align:center">'
                'YOUR FAN IDENTITY</div>',
                unsafe_allow_html=True
            )

            photo = st.session_state.get("profile_photo")

            if photo is not None:
                st.image(
                    photo,
                    width=150,
                    caption="Your profile picture"
                )
            else:
                st.markdown(
                    """
                    <div style="display:flex;justify-content:center;
                        margin:20px 0">
                      <div style="width:130px;height:130px;
                          border-radius:50%;
                          background:linear-gradient(135deg,
                          #30486a,#ff5268);
                          border:4px solid #42dfb9;
                          display:flex;align-items:center;
                          justify-content:center;
                          font-size:57px;
                          box-shadow:0 0 28px #42dfb933">
                          👤
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                f"""
                <div style="text-align:center">
                    <div style="font-size:22px;font-weight:900">
                        {st.session_state.fan_name}
                    </div>
                    <div style="margin-top:9px">
                        <span style="background:#123b32;
                            color:#42dfb9;padding:6px 10px;
                            border-radius:20px;font-size:10px;
                            font-weight:800">
                            ✓ DEMO VERIFIED FAN
                        </span>
                    </div>
                    <div style="color:#9aa9bf;font-size:12px;
                        margin-top:12px">
                        {st.session_state.fan_tier}
                        · LALIGA Community
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.divider()

            st.metric("TruthRank", "92/100", "+3 demo points")
            st.metric("Authenticity Score", "94%")

            st.markdown(
                f"""
                <div style="background:#123b32;color:#42dfb9;
                    padding:12px;border-radius:10px;
                    text-align:center;font-weight:800">
                    🔥 {st.session_state.streak}-Day
                    Belonging Streak
                </div>
                """,
                unsafe_allow_html=True
            )

    with stats_col:
        with st.container(border=True):
            st.markdown("#### Your Fan Impact")

            a, b = st.columns(2)

            a.metric(
                "Belonging Points",
                f"{st.session_state.bp:,}"
            )

            b.metric(
                "Community Rank",
                "#5 demo",
                "Illustrative"
            )

            st.markdown("**TruthRank progress**")
            st.progress(0.92)
            st.caption("92% · Sample profile score")

            st.markdown("**Belonging Points progress**")
            st.progress(min(st.session_state.bp / 10000, 1.0))
            st.caption("Goal: 10,000 BP")

            st.info(
                "Profile scores and verification are demo values, "
                "not independently verified fan credentials."
            )

# ---------------- DASHBOARD PAGE ------------------

if page == "Fan Dashboard":

    render_profile()

    st.divider()
    st.markdown("### ⚽ Match Preview")

    c1, c2, c3 = st.columns([2, 1, 2])

    with c1:
        st.markdown(
            '<div class="club"><div class="club-icon">⚪</div>'
            '<div class="club-name">REAL MADRID</div></div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div style="text-align:center;padding-top:22px;'
            'font-weight:900;font-size:20px;color:#9aa9bf">'
            'VS</div>',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            '<div class="club"><div class="club-icon">🔵🔴</div>'
            '<div class="club-name">BARCELONA</div></div>',
            unsafe_allow_html=True
        )

    st.caption(
        "Demo fixture · No live fixture or score feed connected."
    )

    if st.button("Open Match Center", use_container_width=True):
        st.info("Select Match Center in the sidebar to make a prediction.")

# ---------------- MATCH CENTER --------------------

elif page == "Match Center":

    st.markdown("### ⚽ Match Center")

    st.markdown(
        '<span class="pill">● SIMULATED MATCH</span>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    a, b, c = st.columns([2, 1, 2])

    with a:
        st.markdown(
            '<div class="club"><div class="club-icon">⚪</div>'
            '<div class="club-name">REAL MADRID</div></div>',
            unsafe_allow_html=True
        )

    with b:
        st.markdown(
            '<div style="text-align:center;padding-top:22px;'
            'font-weight:900;font-size:20px">VS</div>',
            unsafe_allow_html=True
        )

    with c:
        st.markdown(
            '<div class="club"><div class="club-icon">🔵🔴</div>'
            '<div class="club-name">BARCELONA</div></div>',
            unsafe_allow_html=True
        )

    st.divider()

    probabilities = {
        "Real Madrid Win": 47,
        "Draw": 22,
        "Barcelona Win": 31
    }

    st.markdown("#### Illustrative Match Probabilities")

    for label, value in probabilities.items():
        col1, col2 = st.columns([4, 1])

        col1.write(label)
        col2.markdown(
            f"<div style='text-align:right;font-weight:900'>"
            f"{value}%</div>",
            unsafe_allow_html=True
        )

        st.progress(value / 100)

    st.caption(
        "Illustrative figures only. These are not live odds "
        "or verified forecasts."
    )

    st.divider()
    st.markdown("#### 🎯 Submit Your Prediction")

    choice = st.radio(
        "Who do you think will win?",
        list(probabilities.keys()),
        key="match_prediction"
    )

    if st.button("Submit Prediction · +25 BP",
                 use_container_width=True):

        if st.session_state.submitted:
            st.warning(
                "You have already submitted a prediction "
                "for this demo match."
            )
        else:
            st.session_state.prediction = choice
            st.session_state.bp += 25
            st.session_state.submitted = True
            st.success(
                f"Prediction saved: {choice}. "
                "25 demo BP awarded!"
            )
            st.rerun()

    if st.session_state.submitted:
        st.info(
            f"Your saved prediction: {st.session_state.prediction}"
        )

# ---------------- LEADERBOARD ---------------------

elif page == "Leaderboard":

    st.markdown("### 🏆 Fan Community Leaderboard")

    leaderboard = st.session_state.cases.copy()

    leaderboard.loc[
        leaderboard["Fan"] == "You", "BP"
    ] = st.session_state.bp

    leaderboard = leaderboard.sort_values(
        "BP", ascending=False
    ).reset_index(drop=True)

    leaderboard.insert(
        0, "Rank", range(1, len(leaderboard) + 1)
    )

    st.dataframe(
        leaderboard,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Rank": st.column_config.NumberColumn(
                "Rank", format="#%d"
            ),
            "BP": st.column_config.NumberColumn(
                "Belonging Points", format="%d"
            )
        }
    )

    your_row = leaderboard[
        leaderboard["Fan"] == "You"
    ]

    if not your_row.empty:
        rank = int(your_row.iloc[0]["Rank"])
        st.metric("Your Current Demo Rank", f"#{rank}")

    st.caption(
        "Other fan accounts are sample data. "
        "This leaderboard is not connected to real users."
    )

    st.download_button(
        "Download Leaderboard CSV",
        data=leaderboard.to_csv(index=False).encode("utf-8"),
        file_name="brodix_fan_leaderboard.csv",
        mime="text/csv"
    )

# ---------------- FAN SETTINGS --------------------

elif page == "Fan Settings":

    st.markdown("### ⚙️ Customize Your Fan Profile")

    st.write(
        "Upload a profile photo and personalize your displayed fan name."
    )

    new_name = st.text_input(
        "Fan display name",
        value=st.session_state.fan_name,
        max_chars=40
    )

    photo = st.file_uploader(
        "Upload profile picture",
        type=["jpg", "jpeg", "png", "webp"],
        help="Choose an image from your phone or computer."
    )

    if photo is not None:
        st.image(photo, width=180, caption="Profile preview")

    if st.button("Save Profile", use_container_width=True):

        if new_name.strip():
            st.session_state.fan_name = new_name.strip()

        if photo is not None:
            # Keep the image bytes in the current session.
            st.session_state.profile_photo = photo.getvalue()

        st.success("Your demo profile has been updated.")
        st.rerun()

    st.divider()

    st.markdown("#### Belonging Streak")

    st.metric(
        "Current Demo Streak",
        f"{st.session_state.streak} days"
    )

    st.caption(
        "Streak progression is not yet linked to a real "
        "daily check-in system."
    )

    st.warning(
        "Profile changes and uploaded images are stored in "
        "the current Streamlit session only. Production "
        "accounts require secure persistent storage."
    )

# ---------------- FOOTER --------------------------

st.divider()

st.markdown(
    """
    <div class="footer">
        BRODIX FAN COMPASS · LALIGA BELONGING OS<br><br>
        Independent innovation prototype. Not an official
        LALIGA product or verified affiliation.<br>
        Demo statistics, identities, predictions and rankings
        are illustrative.
    </div>
    """,
    unsafe_allow_html=True
)
