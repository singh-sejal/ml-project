import html
import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="IPL Win Predictor",
    layout="wide",
)

team = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad"
]

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Jaipur', 'Chennai',
       'Kolkata', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Dharamsala', 'Pune', 'Hyderabad', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Cuttack', 'Visakhapatnam', 'Rajkot', 'Kanpur',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']


@st.cache_resource
def load_model():
    model_path = Path(__file__).resolve().parent / "pikle.pkl"
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)


pipe = load_model()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@600;700&display=swap');

    :root {
        color-scheme: dark;
        --page: #0A0F1C;
        --card: #111827;
        --input: #0A0F1C;
        --border: #1F2937;
        --gold: #F5A524;
        --text: #F3F4F6;
        --muted: #9CA3AF;
    }

    html, body, [class*="css"], [data-testid="stAppViewContainer"] {
        font-family: "Inter", sans-serif;
        color: var(--text);
    }

    .stApp,
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(ellipse at 50% 0%, rgba(245, 165, 36, 0.08), transparent 34%),
            repeating-linear-gradient(135deg, transparent 0, transparent 7px, rgba(255,255,255,0.012) 8px, transparent 9px),
            var(--page);
    }

    #MainMenu,
    [data-testid="stToolbar"],
    [data-testid="stHeader"],
    footer {
        display: none;
    }

    [data-testid="stMainBlockContainer"] {
        width: 92%;
        max-width: 1400px;
        padding: 32px 32px 80px 32px;
        margin: 0 auto;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 24px;
    }

    .page-heading {
        text-align: center;
        padding: 12px 0 32px;
    }

    .page-heading h1 {
        color: #F3F4F6;
        font-family: "Oswald", sans-serif;
        font-size: clamp(40px, 5vw, 56px);
        font-weight: 700;
        letter-spacing: -0.02em;
        line-height: 1.08;
        margin: 0;
        text-transform: uppercase;
    }

    .page-heading p {
        color: #9CA3AF;
        font-size: 16px;
        margin: 12px 0 16px;
    }

    .heading-rule {
        width: 60px;
        height: 3px;
        background: #F5A524;
        margin: 0 auto;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 14px;
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.16);
        padding: 24px;
    }

    [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {
        gap: 16px;
    }

    .panel-heading {
        color: #F3F4F6;
        font-family: "Oswald", sans-serif;
        font-size: 22px;
        font-weight: 700;
        letter-spacing: 0.045em;
        margin: 0 0 4px;
        text-transform: uppercase;
    }

    .section-heading {
        color: #F3F4F6;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 0.08em;
        margin: 8px 0 0;
        text-transform: uppercase;
    }

    [data-testid="stWidgetLabel"] p,
    .stSelectbox label,
    .stNumberInput label {
        color: #9CA3AF !important;
        font-family: "Inter", sans-serif;
        font-size: 12px !important;
        font-weight: 600;
        letter-spacing: 0.07em;
        text-transform: uppercase;
    }

    [data-baseweb="select"] > div,
    [data-testid="stNumberInputContainer"] {
        min-height: 46px;
        background: #0A0F1C !important;
        border: 1px solid #1F2937 !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    [data-baseweb="select"] > div:focus-within,
    [data-testid="stNumberInputContainer"]:focus-within {
        border-color: #F5A524 !important;
        box-shadow: 0 0 0 1px rgba(245, 165, 36, 0.28) !important;
    }

    [data-baseweb="select"] span,
    [data-baseweb="select"] div,
    [data-testid="stNumberInputContainer"] input {
        color: #F3F4F6 !important;
        font-family: "Inter", sans-serif;
    }

    [data-baseweb="select"] svg,
    [data-testid="stNumberInputContainer"] button {
        color: #9CA3AF !important;
        fill: #9CA3AF;
    }

    [data-baseweb="popover"],
    [role="listbox"] {
        background: #111827 !important;
        border: 1px solid #1F2937 !important;
    }

    [role="option"] {
        color: #F3F4F6 !important;
        background: #111827 !important;
    }

    [role="option"]:hover,
    [aria-selected="true"] {
        background: #1F2937 !important;
    }

    .stButton {
        margin-top: 8px;
    }

    .stButton button {
        min-height: 50px;
        background: linear-gradient(100deg, #F5A524, #F59E0B);
        border: 0;
        border-radius: 10px;
        color: #111827;
        font-family: "Inter", sans-serif;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.075em;
        transition: transform 140ms ease, box-shadow 140ms ease;
    }

    .stButton button:hover {
        color: #111827;
        border: 0;
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(245, 165, 36, 0.18);
    }

    .stButton button:active {
        transform: scale(0.98);
    }

    .stButton button:focus:not(:active) {
        color: #111827;
        border: 0;
        box-shadow: 0 0 0 2px #111827, 0 0 0 4px #F5A524;
    }

    .live-intro {
        color: #9CA3AF;
        font-size: 13px;
        line-height: 1.5;
        margin: -4px 0 4px;
    }

    .metric-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 12px;
    }

    .live-metric {
        min-width: 0;
        background: #0A0F1C;
        border: 1px solid #1F2937;
        border-radius: 10px;
        padding: 14px 16px;
    }

    .live-metric-label {
        color: #9CA3AF;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.07em;
        line-height: 1.4;
        text-transform: uppercase;
    }

    .live-metric-value {
        color: #F3F4F6;
        font-family: "Oswald", sans-serif;
        font-size: 36px;
        font-variant-numeric: tabular-nums;
        font-weight: 600;
        line-height: 1.1;
        margin-top: 7px;
        overflow-wrap: anywhere;
    }

    .live-metric-value.is-accent {
        color: #F5A524;
    }

    .results-card {
        border-top: 1px solid #1F2937;
        margin-top: 8px;
        padding-top: 18px;
        animation: result-fade-in 300ms ease-out both;
    }

    @keyframes result-fade-in {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .results-title {
        color: #F3F4F6;
        font-family: "Oswald", sans-serif;
        font-size: 18px;
        font-weight: 600;
        letter-spacing: 0.04em;
        margin: 0 0 12px;
        text-transform: uppercase;
    }

    .probability-row {
        background: #0A0F1C;
        border: 1px solid #1F2937;
        border-left: 4px solid var(--team-color);
        border-radius: 10px;
        margin: 10px 0;
        padding: 12px 14px;
    }

    .team-csk { --team-color: #F7C948; }
    .team-mi { --team-color: #2D8CFF; }
    .team-rcb { --team-color: #E53935; }
    .team-kkr { --team-color: #9B59B6; }
    .team-dc { --team-color: #3B82F6; }
    .team-srh { --team-color: #F97316; }
    .team-rr { --team-color: #EC4899; }
    .team-pbks { --team-color: #EF4444; }
    .team-gt { --team-color: #64748B; }
    .team-lsg { --team-color: #14B8A6; }

    .probability-row.is-favourite {
        background: #141A25;
    }

    .probability-topline {
        align-items: center;
        display: flex;
        gap: 12px;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    .probability-team {
        color: #F3F4F6;
        font-size: 14px;
        font-weight: 600;
        overflow-wrap: anywhere;
    }

    .probability-value {
        color: #F3F4F6;
        font-family: "Oswald", sans-serif;
        font-size: 28px;
        font-variant-numeric: tabular-nums;
        font-weight: 700;
        line-height: 1;
        white-space: nowrap;
    }

    .is-favourite .probability-value {
        color: #F5A524;
    }

    .progress-track {
        appearance: none;
        background: transparent;
        border: 0;
        height: 9px;
        vertical-align: top;
        width: 100%;
    }

    .progress-track::-webkit-progress-bar {
        background: #1F2937;
        border-radius: 8px;
    }

    .progress-track::-webkit-progress-value {
        background: var(--team-color);
        border-radius: 8px;
    }

    .progress-track::-moz-progress-bar {
        background: var(--team-color);
        border-radius: 8px;
    }

    .progress-track::-webkit-progress-value {
        transition: none;
    }

    .match-context {
        color: #D1D5DB;
        font-size: 13px;
        line-height: 1.5;
        margin: 16px 0 12px;
    }

    .favourite-badge {
        background: rgba(245, 165, 36, 0.1);
        border: 1px solid rgba(245, 165, 36, 0.28);
        border-radius: 6px;
        color: #F5A524;
        display: inline-block;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.07em;
        padding: 7px 10px;
        text-transform: uppercase;
    }

    .app-footer {
        align-items: center;
        background: #0A0F1C;
        border-top: 1px solid #1F2937;
        bottom: 0;
        color: #9CA3AF;
        display: flex;
        font-family: "Inter", sans-serif;
        font-size: 13px;
        height: 44px;
        justify-content: center;
        left: 0;
        position: fixed;
        width: 100%;
        z-index: 999;
    }

    @media (max-width: 900px) {
        [data-testid="stMainBlockContainer"] {
            width: 96%;
            padding: 24px 20px 80px;
        }

        [data-testid="stHorizontalBlock"] {
            gap: 16px;
        }
    }

    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] {
            width: 100%;
            padding: 16px 16px 80px;
        }

        .page-heading {
            padding: 12px 0 24px;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            padding: 18px;
        }

        .probability-team {
            font-size: 13px;
        }

        .live-metric {
            padding: 12px;
        }

        .live-metric-value {
            font-size: 32px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="page-heading">
        <h1>IPL WIN PREDICTOR</h1>
        <p>Predict the game. Understand the odds.</p>
        <div class="heading-rule"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

setup_column, live_column = st.columns([1.5, 1], gap="large")

with setup_column:
    with st.container(border=True):
        st.markdown('<div class="panel-heading">Match Setup</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-heading">Match setup</div>', unsafe_allow_html=True)
        batting_column, bowling_column = st.columns(2)
        with batting_column:
            batting_team = st.selectbox("Batting team", sorted(team), index=0)
        with bowling_column:
            bowling_team = st.selectbox("Bowling team", sorted(team), index=1)
        selected_city = st.selectbox("Host city", sorted(cities))

        st.markdown('<div class="section-heading">Match situation</div>', unsafe_allow_html=True)
        target_column, score_column = st.columns(2)
        with target_column:
            target = st.number_input("Target", min_value=1, max_value=300, value=180, step=1)
        with score_column:
            score = st.number_input("Current score", min_value=0, max_value=300, value=120, step=1)

        over_column, wickets_column = st.columns(2)
        with over_column:
            over = st.number_input(
                "Overs done",
                min_value=0.0,
                max_value=20.0,
                value=14.0,
                step=0.1,
                format="%.1f",
            )
        with wickets_column:
            wickets = st.number_input(
                "Wickets down",
                min_value=0,
                max_value=10,
                value=4,
                step=1,
            )

        predict = st.button(
            "PREDICT WIN PROBABILITY",
            type="primary",
            use_container_width=True,
        )

preview_runs_left = target - score
preview_balls_left = max(120 - int(round(over * 6)), 0)
preview_wickets_remaining = 10 - wickets
preview_crr = score / over if over != 0 else None
preview_rrr = (
    (preview_runs_left * 6) / preview_balls_left
    if preview_balls_left != 0
    else None
)

prediction_error = None
prediction_result = None

if predict:
    if batting_team == bowling_team:
        prediction_error = "Please select two different teams."
    elif score > target:
        prediction_error = "The current score cannot be greater than the target."
    elif over == 0:
        prediction_error = "Overs completed must be greater than 0."
    elif wickets == 10:
        prediction_error = "All wickets are lost, so no chase is remaining."
    else:
        runs_left = target - score
        balls_left = max(120 - int(round(over * 6)), 0)

        if balls_left == 0:
            prediction_error = "No balls remain. The target chase is complete."
        else:
            wickets_remaining = 10 - wickets
            crr = score / over
            rrr = (runs_left * 6) / balls_left

            input_df = pd.DataFrame(
                {
                    "batting_team": [batting_team],
                    "bowling_team": [bowling_team],
                    "city": [selected_city],
                    "runs_left": [runs_left],
                    "balls_left": [balls_left],
                    "wickets": [wickets_remaining],
                    "total_runs_x": [target],
                    "crr": [crr],
                    "rrr": [rrr],
                }
            )

            result = pipe.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]
            win_percent = round(win * 100)
            loss_percent = 100 - win_percent
            prediction_result = {
                "loss": loss,
                "loss_percent": loss_percent,
                "win": win,
                "win_percent": win_percent,
                "runs_left": runs_left,
                "balls_left": balls_left,
            }

with live_column:
    with st.container(border=True):
        st.markdown('<div class="panel-heading">Live Match Center</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="live-intro">Match conditions update as you adjust the setup.</div>',
            unsafe_allow_html=True,
        )

        current_rate_text = f"{preview_crr:.2f}" if preview_crr is not None else "—"
        required_rate_text = f"{preview_rrr:.2f}" if preview_rrr is not None else "—"
        live_metrics = [
            ("Runs needed", str(preview_runs_left), False),
            ("Balls left", str(preview_balls_left), False),
            ("Current run rate", current_rate_text, False),
            ("Required run rate", required_rate_text, True),
            ("Wickets in hand", str(preview_wickets_remaining), False),
            ("Target", str(target), False),
        ]
        metrics_html = "".join(
            (
                '<div class="live-metric">'
                f'<div class="live-metric-label">{label}</div>'
                f'<div class="live-metric-value{" is-accent" if is_accent else ""}">{value}</div>'
                "</div>"
            )
            for label, value, is_accent in live_metrics
        )
        st.markdown(
            f'<div class="metric-grid">{metrics_html}</div>',
            unsafe_allow_html=True,
        )

        if prediction_error:
            st.error(prediction_error)

        if prediction_result:
            team_details = {
                "Chennai Super Kings": ("CSK", "team-csk"),
                "Mumbai Indians": ("MI", "team-mi"),
                "Royal Challengers Bengaluru": ("RCB", "team-rcb"),
                "Kolkata Knight Riders": ("KKR", "team-kkr"),
                "Delhi Capitals": ("DC", "team-dc"),
                "Sunrisers Hyderabad": ("SRH", "team-srh"),
                "Rajasthan Royals": ("RR", "team-rr"),
                "Punjab Kings": ("PBKS", "team-pbks"),
                "Gujarat Titans": ("GT", "team-gt"),
                "Lucknow Super Giants": ("LSG", "team-lsg"),
            }
            win_team = html.escape(batting_team)
            loss_team = html.escape(bowling_team)
            win_abbreviation, win_css_class = team_details[batting_team]
            loss_abbreviation, loss_css_class = team_details[bowling_team]
            batting_favourite = prediction_result["win"] >= prediction_result["loss"]
            win_value = prediction_result["win"]
            loss_value = prediction_result["loss"]
            win_percent = prediction_result["win_percent"]
            loss_percent = prediction_result["loss_percent"]
            tied = win_value == loss_value
            favourite = (
                "EVEN"
                if tied
                else win_abbreviation if batting_favourite else loss_abbreviation
            )
            win_row_class = " is-favourite" if batting_favourite and not tied else ""
            loss_row_class = " is-favourite" if not batting_favourite and not tied else ""
            context = (
                f"{win_abbreviation} need {prediction_result['runs_left']} runs "
                f"off {prediction_result['balls_left']} balls."
            )

            st.markdown(
                f"""
                <section class="results-card">
                    <h2 class="results-title">Win Probability</h2>
                    <div class="probability-row {win_css_class}{win_row_class}">
                        <div class="probability-topline">
                            <span class="probability-team">{win_team}</span>
                            <span class="probability-value">{win_percent}%</span>
                        </div>
                        <progress class="progress-track {win_css_class}" value="{win_value:.8f}" max="1">{win_percent}%</progress>
                    </div>
                    <div class="probability-row {loss_css_class}{loss_row_class}">
                        <div class="probability-topline">
                            <span class="probability-team">{loss_team}</span>
                            <span class="probability-value">{loss_percent}%</span>
                        </div>
                        <progress class="progress-track {loss_css_class}" value="{loss_value:.8f}" max="1">{loss_percent}%</progress>
                    </div>
                    <p class="match-context">{context}</p>
                    <span class="favourite-badge">Favourite: {favourite}</span>
                </section>
                """,
                unsafe_allow_html=True,
            )

st.markdown('<div class="app-footer">Made by Akash</div>', unsafe_allow_html=True)
