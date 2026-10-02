import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE
# =========================================================

st.set_page_config(
    page_title="Meta Ads Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #08080a;
    color: #ffffff;
}

header[data-testid="stHeader"] {
    background: #08080a !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

[data-testid="stSidebar"] {
    background: #050506;
    border-right: 1px solid #25252a;
}

.block-container {
    padding: 28px 38px;
    max-width: 1500px;
}

h1, h2, h3, p, label {
    color: #ffffff !important;
}

.dashboard-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 4px;
}

.subtitle {
    color: #92929b !important;
    font-size: 14px;
    margin-bottom: 25px;
}

.section {
    font-size: 19px;
    font-weight: 700;
    margin-top: 24px;
    margin-bottom: 12px;
}

.brand {
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 35px;
}

.brand span {
    color: #7040ff;
}

.card {
    background: #141416;
    border: 1px solid #29292f;
    border-radius: 15px;
    padding: 18px;
    min-height: 105px;
}

.card-label {
    color: #9999a2;
    font-size: 11px;
    text-transform: uppercase;
}

.card-value {
    color: #ffffff;
    font-size: 27px;
    font-weight: 800;
    margin-top: 9px;
}

.card-note {
    color: #8066ff;
    font-size: 11px;
    margin-top: 6px;
}

.panel {
    background: #121214;
    border: 1px solid #29292f;
    border-radius: 15px;
    padding: 15px;
}

.insight {
    background: linear-gradient(135deg, #24105e, #111116);
    border: 1px solid #402487;
    border-radius: 15px;
    padding: 20px;
    min-height: 135px;
}

.insight-title {
    color: #bcaeff;
    font-size: 11px;
    font-weight: 700;
}

.insight-value {
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-top: 15px;
}

.insight-text {
    color: #a5a5ad;
    font-size: 12px;
    margin-top: 8px;
}

/* Purple multiselect tags */
.stMultiSelect [data-baseweb="tag"] {
    background-color: #6336e8 !important;
    border-radius: 8px !important;
}

.stMultiSelect [data-baseweb="tag"] span {
    color: white !important;
}

/* Dark input boxes */
div[data-baseweb="select"] > div {
    background-color: #151517 !important;
    border-color: #303038 !important;
}

input {
    background-color: #151517 !important;
    color: white !important;
}

[data-testid="stDateInput"] input {
    background-color: #151517 !important;
    color: white !important;
}

/* Radio buttons */
[data-testid="stRadio"] label {
    color: #bdbdc5 !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: #141416;
    border: 1px solid #29292f;
    border-radius: 14px;
    padding: 14px;
}

[data-testid="stMetricLabel"] {
    color: #9999a2 !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    df = pd.read_csv("data/meta_ads_sample.csv")

    df["date"] = pd.to_datetime(df["date"])

    numeric_columns = [
        "spend",
        "impressions",
        "reach",
        "clicks",
        "conversions",
        "leads"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        ).fillna(0)

    return df


df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">◕ ADS<span>TIV</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### Dashboard"
    )

    page = st.radio(
        "View",
        [
            "Overview",
            "Campaigns",
            "Platforms"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.caption("META ADS CAMPAIGN INTELLIGENCE")

    st.markdown(
        """
        <div class="insight">
        <div class="insight-title">PORTFOLIO PROJECT</div>
        <div class="insight-value">Meta Ads Analytics</div>
        <div class="insight-text">
        Facebook & Instagram campaign performance dashboard.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="dashboard-title">Meta Ads Performance Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Facebook & Instagram Campaign Performance Dashboard</div>',
    unsafe_allow_html=True
)

# =========================================================
# FILTERS
# =========================================================

filter1, filter2, filter3 = st.columns([1.2, 1.5, 1])

with filter1:

    dates = st.date_input(
        "Date Range",
        value=(
            df["date"].min().date(),
            df["date"].max().date()
        )
    )

with filter2:

    campaigns = st.multiselect(
        "Campaign",
        sorted(df["campaign"].unique()),
        default=sorted(df["campaign"].unique())
    )

with filter3:

    platforms = st.multiselect(
        "Platform",
        sorted(df["platform"].unique()),
        default=sorted(df["platform"].unique())
    )

# =========================================================
# FILTER DATA
# =========================================================

data = df.copy()

if len(dates) == 2:

    data = data[
        (data["date"].dt.date >= dates[0]) &
        (data["date"].dt.date <= dates[1])
    ]

if campaigns:

    data = data[
        data["campaign"].isin(campaigns)
    ]

if platforms:

    data = data[
        data["platform"].isin(platforms)
    ]

# =========================================================
# KPI CALCULATIONS
# =========================================================

spend = data["spend"].sum()
impressions = data["impressions"].sum()
clicks = data["clicks"].sum()
conversions = data["conversions"].sum()
leads = data["leads"].sum()

ctr = (
    clicks / impressions * 100
    if impressions > 0 else 0
)

cpc = (
    spend / clicks
    if clicks > 0 else 0
)

cost_conversion = (
    spend / conversions
    if conversions > 0 else 0
)

# =========================================================
# KPI CARDS
# =========================================================

st.markdown(
    '<div class="section">Campaign Overview</div>',
    unsafe_allow_html=True
)

k1, k2, k3, k4 = st.columns(4)

cards = [
    ("TOTAL SPEND", f"₹{spend:,.0f}", "Campaign Investment"),
    ("IMPRESSIONS", f"{impressions:,.0f}", "Total Ad Views"),
    ("CLICKS", f"{clicks:,.0f}", f"CTR {ctr:.2f}%"),
    ("CONVERSIONS", f"{conversions:,.0f}", f"₹{cost_conversion:.2f} / conversion")
]

for col, item in zip(
    [k1, k2, k3, k4],
    cards
):

    title, value, note = item

    col.markdown(
        f"""
        <div class="card">
        <div class="card-label">{title}</div>
        <div class="card-value">{value}</div>
        <div class="card-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# SECOND KPI ROW
# =========================================================

k1, k2, k3, k4 = st.columns(4)

k1.metric("CTR", f"{ctr:.2f}%")
k2.metric("CPC", f"₹{cpc:.2f}")
k3.metric("LEADS", f"{leads:,.0f}")
k4.metric("COST / CONVERSION", f"₹{cost_conversion:.2f}")

# =========================================================
# ANALYTICS
# =========================================================

st.markdown(
    '<div class="section">Performance Analytics</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1.15, 1])

daily = data.groupby(
    "date",
    as_index=False
).agg(
    spend=("spend", "sum"),
    conversions=("conversions", "sum")
)

with left:

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=daily["date"],
            y=daily["spend"],
            mode="lines",
            name="Spend",
            line=dict(
                color="#6937ff",
                width=3
            ),
            fill="tozeroy",
            fillcolor="rgba(105,55,255,0.15)"
        )
    )

    fig.update_layout(
        title="Daily Ad Spend",
        template="plotly_dark",
        height=330,
        paper_bgcolor="#121214",
        plot_bgcolor="#121214",
        margin=dict(
            l=10,
            r=10,
            t=50,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    mix = data.groupby(
        "platform",
        as_index=False
    )["conversions"].sum()

    fig = px.pie(
        mix,
        names="platform",
        values="conversions",
        hole=0.68,
        title="Conversion Mix",
        color_discrete_sequence=[
            "#5b22ff",
            "#b9a5ff"
        ]
    )

    fig.update_layout(
        template="plotly_dark",
        height=330,
        paper_bgcolor="#121214"
    )

    fig.add_annotation(
        text=f"<b>{conversions:,.0f}</b><br>Conversions",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(
            size=16,
            color="white"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# CAMPAIGN PERFORMANCE
# =========================================================

campaign = data.groupby(
    "campaign",
    as_index=False
).agg(
    spend=("spend", "sum"),
    impressions=("impressions", "sum"),
    clicks=("clicks", "sum"),
    conversions=("conversions", "sum"),
    leads=("leads", "sum")
)

campaign["ctr"] = (
    campaign["clicks"] /
    campaign["impressions"].replace(0, pd.NA)
) * 100

campaign["cpc"] = (
    campaign["spend"] /
    campaign["clicks"].replace(0, pd.NA)
)

campaign["cost_conversion"] = (
    campaign["spend"] /
    campaign["conversions"].replace(0, pd.NA)
)

campaign = campaign.fillna(0)

# =========================================================
# CAMPAIGN PAGE
# =========================================================

if page in ["Overview", "Campaigns"]:

    st.markdown(
        '<div class="section">Campaign Performance</div>',
        unsafe_allow_html=True
    )

    a, b = st.columns(2)

    with a:

        fig = px.bar(
            campaign,
            x="campaign",
            y="spend",
            title="Spend by Campaign",
            color="spend",
            color_continuous_scale=[
                "#24105e",
                "#6c35ff",
                "#b9a5ff"
            ]
        )

        fig.update_layout(
            template="plotly_dark",
            height=340,
            paper_bgcolor="#121214",
            plot_bgcolor="#121214",
            coloraxis_showscale=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with b:

        fig = px.bar(
            campaign,
            x="campaign",
            y="conversions",
            title="Conversions by Campaign",
            color="conversions",
            color_continuous_scale=[
                "#24105e",
                "#6c35ff",
                "#b9a5ff"
            ]
        )

        fig.update_layout(
            template="plotly_dark",
            height=340,
            paper_bgcolor="#121214",
            plot_bgcolor="#121214",
            coloraxis_showscale=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================================================
# PLATFORM
# =========================================================

if page in ["Overview", "Platforms"]:

    st.markdown(
        '<div class="section">Facebook vs Instagram</div>',
        unsafe_allow_html=True
    )

    platform = data.groupby(
        "platform",
        as_index=False
    ).agg(
        spend=("spend", "sum"),
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        conversions=("conversions", "sum")
    )

    platform["ctr"] = (
        platform["clicks"] /
        platform["impressions"].replace(0, pd.NA)
    ) * 100

    platform["cost_conversion"] = (
        platform["spend"] /
        platform["conversions"].replace(0, pd.NA)
    )

    platform = platform.fillna(0)

    a, b = st.columns(2)

    with a:

        fig = px.bar(
            platform,
            x="platform",
            y="ctr",
            title="CTR by Platform",
            color="platform",
            color_discrete_sequence=[
                "#6937ff",
                "#b9a5ff"
            ]
        )

        fig.update_layout(
            template="plotly_dark",
            height=300,
            paper_bgcolor="#121214",
            plot_bgcolor="#121214"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with b:

        fig = px.bar(
            platform,
            x="platform",
            y="cost_conversion",
            title="Cost per Conversion",
            color="platform",
            color_discrete_sequence=[
                "#6937ff",
                "#ef6cff"
            ]
        )

        fig.update_layout(
            template="plotly_dark",
            height=300,
            paper_bgcolor="#121214",
            plot_bgcolor="#121214"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================================================
# BUSINESS INSIGHTS
# =========================================================

st.markdown(
    '<div class="section">Business Insights</div>',
    unsafe_allow_html=True
)

if len(campaign) > 0:

    best = campaign.loc[
        campaign["conversions"].idxmax(),
        "campaign"
    ]

    expensive = campaign.loc[
        campaign["cost_conversion"].idxmax(),
        "campaign"
    ]

else:

    best = "-"
    expensive = "-"

a, b, c = st.columns(3)

with a:

    st.markdown(
        f"""
        <div class="insight">
        <div class="insight-title">TOP CONVERSION CAMPAIGN</div>
        <div class="insight-value">{best}</div>
        <div class="insight-text">
        Highest conversion volume in the selected data.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with b:

    st.markdown(
        f"""
        <div class="insight">
        <div class="insight-title">HIGH COST / CONVERSION</div>
        <div class="insight-value">{expensive}</div>
        <div class="insight-text">
        Campaign with the highest acquisition cost.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c:

    st.markdown(
        f"""
        <div class="insight">
        <div class="insight-title">DATASET</div>
        <div class="insight-value">{len(data):,} Rows</div>
        <div class="insight-text">
        Synthetic portfolio dataset used for demonstration.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "Meta Ads Campaign Intelligence • "
    "Python • Pandas • Plotly • Streamlit • "
    "Portfolio Project"
)