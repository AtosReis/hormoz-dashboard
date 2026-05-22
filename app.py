import streamlit as st
from pathlib import Path
import pandas as pd
import base64

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def find_file_by_keywords(keywords):
    files = list(DATA_DIR.glob("*"))
    for file in files:
        name = file.name.lower()
        if all(k.lower() in name for k in keywords):
            return file
    return None


LOGO_WHITE = find_file_by_keywords(["logo", "quantse", "branco"])
LOGO_BLACK = find_file_by_keywords(["logo", "quantse", "preto"])


st.set_page_config(
    page_title="Hormoz | Multi-Asset Strategy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Data
# -----------------------------

def find_image(possible_keywords):
    files = list(DATA_DIR.glob("*"))
    for keywords in possible_keywords:
        for file in files:
            name = file.name.lower()
            if all(k.lower() in name for k in keywords):
                return file
    return None


strategies = {
    "SP500 / ES=F": {
        "market": "SP500",
        "symbol": "ES=F",
        "magic": "7649082163",
        "date": "19/05/2026",
        "leverage": "2",
        "portfolio_size": "10",
        "image": find_image([["SP500", "ES"], ["SP500"], ["ES_F"]]),
        "annual_return": 82.68,
        "monthly_return": 5.15,
        "last_month_return": -1.18,
        "annual_vol": 17.30,
        "monthly_vol": 5.11,
        "daily_vol": 1.09,
        "sharpe": 0.23,
        "sqn": 6.18,
        "max_loss": -5.79,
        "max_drawdown": -9.88,
        "success_rate": 87.95,
        "mean_gain": 0.43,
        "mean_loss": -1.09,
        "gain_loss_ratio": 0.393,
        "oos_pvalue": 92.48
    },
    "DJI30 / YM=F": {
        "market": "DJI30",
        "symbol": "YM=F",
        "magic": "74983545",
        "date": "19/05/2026",
        "leverage": "3",
        "portfolio_size": "10",
        "image": find_image([["DJI30", "YM"], ["DJI30"], ["YM_F"]]),
        "annual_return": 91.29,
        "monthly_return": 5.55,
        "last_month_return": 7.72,
        "annual_vol": 23.08,
        "monthly_vol": 6.82,
        "daily_vol": 1.45,
        "sharpe": 0.18,
        "sqn": 5.07,
        "max_loss": -6.75,
        "max_drawdown": -17.35,
        "success_rate": 88.61,
        "mean_gain": 0.54,
        "mean_loss": -1.85,
        "gain_loss_ratio": 0.293,
        "oos_pvalue": 79.29
    },
    "NASDAQ100 / NQ=F": {
        "market": "NASDAQ100",
        "symbol": "NQ=F",
        "magic": "879856457",
        "date": "19/05/2026",
        "leverage": "2",
        "portfolio_size": "10",
        "image": find_image([["NDQ100"], ["NASDAQ"], ["NQ"], ["NO_F"]]),
        "annual_return": 94.18,
        "monthly_return": 5.69,
        "last_month_return": 8.30,
        "annual_vol": 20.48,
        "monthly_vol": 6.05,
        "daily_vol": 1.29,
        "sharpe": 0.21,
        "sqn": 5.79,
        "max_loss": -6.30,
        "max_drawdown": -13.33,
        "success_rate": 87.81,
        "mean_gain": 0.52,
        "mean_loss": -1.50,
        "gain_loss_ratio": 0.345,
        "oos_pvalue": 72.45
    },
    "GOLD / GC=F": {
        "market": "GOLD",
        "symbol": "GC=F",
        "magic": "-",
        "date": "19/05/2026",
        "leverage": "-",
        "portfolio_size": "10",
        "image": find_image([["GOLD", "GC"], ["GOLD"], ["GC_F"]]),
        "annual_return": 6.31,
        "monthly_return": 0.51,
        "last_month_return": -3.18,
        "annual_vol": 19.36,
        "monthly_vol": 5.72,
        "daily_vol": 1.22,
        "sharpe": 0.03,
        "sqn": 0.72,
        "max_loss": -11.58,
        "max_drawdown": -28.29,
        "success_rate": 87.28,
        "mean_gain": 0.28,
        "mean_loss": -1.66,
        "gain_loss_ratio": 0.168,
        "oos_pvalue": 71.13
    }
,
    "US Oil / CL=F": {
        "market": "US Oil",
        "symbol": "CL=F",
        "magic": "-",
        "date": "19/05/2026",
        "leverage": "-",
        "portfolio_size": "10",
        "image": find_image([["USOil", "CL"], ["USOil"], ["CL_F"], ["Oil"]]),
        "annual_return": 61.11,
        "monthly_return": 4.05,
        "last_month_return": 3.77,
        "annual_vol": 20.73,
        "monthly_vol": 6.13,
        "daily_vol": 1.31,
        "sharpe": 0.15,
        "sqn": 4.17,
        "max_loss": -8.78,
        "max_drawdown": -29.48,
        "success_rate": 88.21,
        "mean_gain": 0.46,
        "mean_loss": -1.74,
        "gain_loss_ratio": 0.262,
        "oos_pvalue": 94.04
    }

}


portfolio_data = {
    "market": "4-Asset Portfolio",
    "symbol": "DJI30 + NDQ100 + SP500 + US Oil",
    "magic": "-",
    "date": "19/05/2026",
    "leverage": "-",
    "portfolio_size": "4",
    "image": find_image([["portfoil", "DJ30", "NDQ100", "SP500", "USOil"], ["portfoil_DJ30_NDQ100_SP500_USOil"], ["NDQ100", "USOil"]]),
    "annual_return": 85.95,
    "monthly_return": 5.31,
    "last_month_return": 5.08,
    "annual_vol": 15.96,
    "monthly_vol": 4.72,
    "daily_vol": 1.01,
    "sharpe": 0.25,
    "sqn": 6.88,
    "max_loss": -7.38,
    "max_drawdown": -18.03,
    "success_rate": 78.81,
    "mean_gain": 0.54,
    "mean_loss": -0.83,
    "gain_loss_ratio": 0.653,
    "oos_pvalue": 25.35
}


portfolio_3assets_2x_data = {
    "market": "3-Asset Portfolio 2x",
    "symbol": "DJI30 + NDQ100 + SP500",
    "magic": "-",
    "date": "19/05/2026",
    "leverage": "2",
    "portfolio_size": "3",
    "image": find_image([["portfoil", "DJ30", "NDQ100", "SP500", "2x"], ["portfoil_DJ30_NDQ100_SP500_2x"], ["NDQ100", "SP500", "2x"]]),
    "annual_return": 69.65,
    "monthly_return": 4.50,
    "last_month_return": 6.92,
    "annual_vol": 14.31,
    "monthly_vol": 4.23,
    "daily_vol": 0.90,
    "sharpe": 0.24,
    "sqn": 6.52,
    "max_loss": -3.39,
    "max_drawdown": -8.46,
    "success_rate": 81.99,
    "mean_gain": 0.44,
    "mean_loss": -0.84,
    "gain_loss_ratio": 0.532,
    "oos_pvalue": 94.98
}


portfolio_3assets_3x_data = {
    "market": "3-Asset Portfolio 3x",
    "symbol": "DJI30 + NDQ100 + SP500",
    "magic": "-",
    "date": "19/05/2026",
    "leverage": "3",
    "portfolio_size": "3",
    "image": find_image([["portfoil", "DJ30", "NDQ100", "SP500", "3x"], ["portfoil_DJ30_NDQ100_SP500_3x"], ["NDQ100", "SP500", "3x"]]),
    "annual_return": 121.79,
    "monthly_return": 6.86,
    "last_month_return": 4.90,
    "annual_vol": 21.31,
    "monthly_vol": 6.29,
    "daily_vol": 1.34,
    "sharpe": 0.24,
    "sqn": 6.67,
    "max_loss": -6.70,
    "max_drawdown": -12.78,
    "success_rate": 81.72,
    "mean_gain": 0.66,
    "mean_loss": -1.16,
    "gain_loss_ratio": 0.566,
    "oos_pvalue": 51.42
}


def pct(value):
    return f"{value:.2f}%"


def num(value):
    return f"{value:.2f}"


# -----------------------------
# Styling
# -----------------------------

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #f6f8fb 0%, #ffffff 42%);
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1650px;
    }

    [data-testid="stSidebar"] {
        background: #0f172a;
    }

    [data-testid="stSidebar"] img {
        margin-top: 0.5rem;
        margin-bottom: 1.2rem;
        border-radius: 14px;
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #334155 100%);
        color: white;
        padding: 2rem 2.2rem;
        border-radius: 28px;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.18);
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        font-size: 2.2rem;
        margin-bottom: 0.25rem;
        color: white;
    }

    .hero p {
        color: #cbd5e1;
        font-size: 1rem;
        margin-bottom: 0;
    }

    .pill {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        color: #e5e7eb;
        padding: 0.35rem 0.75rem;
        border-radius: 999px;
        font-size: 0.82rem;
        margin-right: 0.35rem;
        margin-top: 0.8rem;
    }

    .kpi-card {
        background: rgba(255,255,255,0.96);
        border: 1px solid #e5e7eb;
        border-radius: 22px;
        padding: 1.1rem 1.15rem;
        box-shadow: 0 8px 26px rgba(15,23,42,0.06);
        min-height: 120px;
    }

    .kpi-label {
        color: #64748b;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 0.35rem;
    }

    .kpi-value {
        color: #0f172a;
        font-size: 1.65rem;
        font-weight: 800;
        letter-spacing: -0.03em;
    }

    .kpi-sub {
        color: #64748b;
        font-size: 0.83rem;
        margin-top: 0.35rem;
    }

    .positive {
        color: #047857;
    }

    .negative {
        color: #b91c1c;
    }

    .neutral {
        color: #0f172a;
    }

    .panel {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 26px;
        padding: 1.4rem 1.5rem;
        box-shadow: 0 8px 28px rgba(15,23,42,0.055);
        margin-top: 1rem;
    }

    .section-header {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.9rem;
    }

    .muted {
        color: #64748b;
        font-size: 0.92rem;
    }

    .small-table-title {
        color: #0f172a;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 6px 22px rgba(15,23,42,0.05);
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Components
# -----------------------------

def signed_class(value):
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "neutral"


def kpi_card(label, value, suffix="", sub="", signed=False):
    color_class = signed_class(value) if signed else "neutral"

    if suffix == "%":
        display_value = pct(value)
    else:
        display_value = num(value) if isinstance(value, float) else str(value)

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value {color_class}">{display_value}</div>
            <div class="kpi-sub">{sub}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def build_comparison_df():
    rows = []
    for name, d in strategies.items():
        rows.append({
            "Strategy": name,
            "Market": d["market"],
            "Symbol": d["symbol"],
            "Magic": d["magic"],
            "Leverage": d["leverage"],
            "Portfolio Size": d["portfolio_size"],
            "Annualized Return": d["annual_return"],
            "Monthly Return": d["monthly_return"],
            "Last Month": d["last_month_return"],
            "Annual Volatility": d["annual_vol"],
            "Sharpe": d["sharpe"],
            "SQN": d["sqn"],
            "Maximum Loss": d["max_loss"],
            "Maximum Drawdown": d["max_drawdown"],
            "Success Rate": d["success_rate"],
            "Mean Gain": d["mean_gain"],
            "Mean Loss": d["mean_loss"],
            "G/L": d["gain_loss_ratio"],
            "OOS p-value": d["oos_pvalue"]
        })
    return pd.DataFrame(rows)


comparison_df = build_comparison_df()


def render_strategy(name, data):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{name}</h1>
            <p>Walk-forward analysis strategy overview, performance metrics and risk profile.</p>
            <span class="pill">Symbol: {data["symbol"]}</span>
            <span class="pill">Magic: {data["magic"]}</span>
            <span class="pill">Leverage: {data["leverage"]}x</span>
            <span class="pill">Portfolio Size: {data["portfolio_size"]}</span>
            <span class="pill">Base date: {data["date"]}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        kpi_card("Annualized Return", data["annual_return"], "%", "Compounded annual performance", signed=True)
    with k2:
        kpi_card("Monthly Return", data["monthly_return"], "%", "Average monthly performance", signed=True)
    with k3:
        kpi_card("Maximum Drawdown", data["max_drawdown"], "%", "Peak-to-trough loss", signed=True)
    with k4:
        kpi_card("SQN", data["sqn"], "", "System quality number")

    k5, k6, k7, k8 = st.columns(4)
    with k5:
        kpi_card("Sharpe Ratio", data["sharpe"], "", "Return adjusted by volatility")
    with k6:
        kpi_card("Success Rate", data["success_rate"], "%", "Winning periods / trades", signed=True)
    with k7:
        kpi_card("Last Month Return", data["last_month_return"], "%", "Most recent monthly result", signed=True)
    with k8:
        kpi_card("Annual Volatility", data["annual_vol"], "%", "Annualized risk level")

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Equity Curve and Return Distribution</div>', unsafe_allow_html=True)

    if data["image"] and data["image"].exists():
        st.image(str(data["image"]), use_container_width=True)
        st.markdown(f'<div class="muted">Source file: {data["image"].name}</div>', unsafe_allow_html=True)
    else:
        st.warning(f"Image not found for {name}. Please check the files inside: {DATA_DIR}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Statistical Breakdown</div>', unsafe_allow_html=True)

    d1, d2, d3, d4 = st.columns(4)

    with d1:
        st.markdown('<div class="small-table-title">Returns</div>', unsafe_allow_html=True)
        st.write(f"Annualized: **{pct(data['annual_return'])} p.a.**")
        st.write(f"Monthly: **{pct(data['monthly_return'])} p.m.**")
        st.write(f"Last month: **{pct(data['last_month_return'])}**")

    with d2:
        st.markdown('<div class="small-table-title">Volatility</div>', unsafe_allow_html=True)
        st.write(f"Annualized: **{pct(data['annual_vol'])} p.a.**")
        st.write(f"Monthly: **{pct(data['monthly_vol'])} p.m.**")
        st.write(f"Daily: **{pct(data['daily_vol'])} p.d.**")

    with d3:
        st.markdown('<div class="small-table-title">Gains and Losses</div>', unsafe_allow_html=True)
        st.write(f"Mean gain G: **{pct(data['mean_gain'])}**")
        st.write(f"Mean loss L: **{pct(data['mean_loss'])}**")
        st.write(f"G/L: **{data['gain_loss_ratio']:.3f}**")

    with d4:
        st.markdown('<div class="small-table-title">Robustness / Test</div>', unsafe_allow_html=True)
        st.write(f"Sharpe Ratio: **{data['sharpe']:.2f}**")
        st.write(f"SQN: **{data['sqn']:.2f}**")
        st.write(f"OOS t-Test p-value: **{pct(data['oos_pvalue'])}**")

    st.markdown('</div>', unsafe_allow_html=True)


def render_comparison():
    st.markdown(
        """
        <div class="hero">
            <h1>Strategy Comparison</h1>
            <p>Side-by-side view of all tested futures strategies.</p>
            <span class="pill">SP500 / ES=F</span>
            <span class="pill">DJI30 / YM=F</span>
            <span class="pill">NASDAQ100 / NQ=F</span>
            <span class="pill">GOLD / GC=F</span>
            <span class="pill">US Oil / CL=F</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    best_return = comparison_df.sort_values("Annualized Return", ascending=False).iloc[0]
    best_drawdown = comparison_df.sort_values("Maximum Drawdown", ascending=False).iloc[0]
    best_sqn = comparison_df.sort_values("SQN", ascending=False).iloc[0]
    best_success = comparison_df.sort_values("Success Rate", ascending=False).iloc[0]

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        kpi_card("Best Annualized Return", best_return["Annualized Return"], "%", best_return["Strategy"], signed=True)
    with c2:
        kpi_card("Lowest Drawdown", best_drawdown["Maximum Drawdown"], "%", best_drawdown["Strategy"], signed=True)
    with c3:
        kpi_card("Best SQN", best_sqn["SQN"], "", best_sqn["Strategy"])
    with c4:
        kpi_card("Best Success Rate", best_success["Success Rate"], "%", best_success["Strategy"], signed=True)


    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">4-Asset Portfolio Highlight</div>', unsafe_allow_html=True)

    p1, p2, p3, p4 = st.columns(4)

    with p1:
        kpi_card("Annualized Return", portfolio_data["annual_return"], "%", "Portfolio / 4 Assets", signed=True)
    with p2:
        kpi_card("Monthly Return", portfolio_data["monthly_return"], "%", "Monthly portfolio performance", signed=True)
    with p3:
        kpi_card("Maximum Drawdown", portfolio_data["max_drawdown"], "%", "Portfolio risk profile", signed=True)
    with p4:
        kpi_card("Sharpe Ratio", portfolio_data["sharpe"], "", "Risk-adjusted return")

    if portfolio_data["image"] and portfolio_data["image"].exists():
        st.image(str(portfolio_data["image"]), use_container_width=True)
        st.markdown(f'<div class="muted">Source file: {portfolio_data["image"].name}</div>', unsafe_allow_html=True)
    else:
        st.warning("Portfolio image not found.")

    st.markdown('</div>', unsafe_allow_html=True)


    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Performance Table</div>', unsafe_allow_html=True)

    display_df = comparison_df.copy()

    percent_cols = [
        "Annualized Return", "Monthly Return", "Last Month", "Annual Volatility",
        "Maximum Loss", "Maximum Drawdown", "Success Rate", "Mean Gain",
        "Mean Loss", "OOS p-value"
    ]

    for col in percent_cols:
        display_df[col] = display_df[col].map(lambda x: f"{x:.2f}%")

    display_df["Sharpe"] = display_df["Sharpe"].map(lambda x: f"{x:.2f}")
    display_df["SQN"] = display_df["SQN"].map(lambda x: f"{x:.2f}")
    display_df["G/L"] = display_df["G/L"].map(lambda x: f"{x:.3f}")

    st.dataframe(display_df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Key Metrics Ranking</div>', unsafe_allow_html=True)

    chart_df = comparison_df.set_index("Strategy")[
        ["Annualized Return", "Annual Volatility", "Maximum Drawdown", "Success Rate", "SQN"]
    ]

    st.bar_chart(chart_df)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Visual Summary</div>', unsafe_allow_html=True)

    visual_cols = st.columns(len(strategies))

    for col, strategy_name in zip(visual_cols, strategies.keys()):
        with col:
            st.markdown(f"### {strategy_name}")
            img = strategies[strategy_name]["image"]

            if img and img.exists():
                st.image(str(img), use_container_width=True)
            else:
                st.warning("Image not found")

    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Sidebar
# -----------------------------

if LOGO_WHITE and LOGO_WHITE.exists():
    st.sidebar.image(str(LOGO_WHITE), use_container_width=True)
else:
    st.sidebar.markdown("## Hormoz")

st.sidebar.markdown("### Multi-Asset Strategy Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "SP500 / ES=F", "DJI30 / YM=F", "NASDAQ100 / NQ=F", "GOLD / GC=F", "US Oil / CL=F", "Portfolio / 4 Assets", "Portfolio / 3 Assets 2x", "Portfolio / 3 Assets 3x"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Dataset")
st.sidebar.write("Base date: **19/05/2026**")
st.sidebar.write("Portfolio size: **10**")
st.sidebar.write("Method: **WFA**")

st.sidebar.markdown("---")
st.sidebar.markdown("### Files detected")
for name, data in strategies.items():
    if data["image"] and data["image"].exists():
        st.sidebar.success(f"{name}")
    else:
        st.sidebar.error(f"{name}")


# -----------------------------
# Main Router
# -----------------------------

if page == "Overview":
    render_comparison()
elif page == "Portfolio / 4 Assets":
    render_strategy(page, portfolio_data)
elif page == "Portfolio / 3 Assets 2x":
    render_strategy(page, portfolio_3assets_2x_data)
elif page == "Portfolio / 3 Assets 3x":
    render_strategy(page, portfolio_3assets_3x_data)
else:
    render_strategy(page, strategies[page])

