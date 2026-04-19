import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data, save_data
from src.data_generator import generate_poll_data
from src.preprocessing import clean_data
from src.analysis import calculate_summary, region_analysis, trend_analysis
from src.filters import apply_filters
from src.config import AGE_GROUPS, REGIONS, OPTIONS

st.set_page_config(layout="wide")

# ======================
# CUSTOM STYLING
# ======================
st.markdown("""
<style>
.big-title {
    font-size:40px;
    font-weight:bold;
    color:#4CAF50;
}
.card {
    padding:20px;
    border-radius:15px;
    background-color:#yellow;
    box-shadow:2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ======================
# NAVIGATION
# ======================
st.sidebar.title("🚀 Poll Visualizer Pro")
page = st.sidebar.radio("Navigate", [
    "🏠 Dashboard",
    "📝 Submit",
    "📊 Advanced Analysis",
    "🌍 Demographics",
    "📈 Trends",
    "🏆 Insights Lab"
])

# ======================
# DATA
# ======================
df = clean_data(load_data())

if st.sidebar.button("⚡ Generate 6000 Data"):
    generate_poll_data(6000)
    st.sidebar.success("Data Generated!")

if df.empty:
    st.warning("No data available")
    st.stop()

# ======================
# 🏠 DASHBOARD (PREMIUM)
# ======================
if page == "🏠 Dashboard":

    st.markdown('<p class="big-title">📊 Executive Dashboard</p>', unsafe_allow_html=True)

    summary = calculate_summary(df)

    total = summary["Count"].sum()
    top = summary["Count"].idxmax()
    percent = round(summary["Percentage"].max(), 2)

    col1, col2, col3 = st.columns(3)

    col1.markdown(f'<div class="card">📌 <b>Total</b><br>{total}</div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="card">🏆 <b>Leader</b><br>{top}</div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="card">📊 <b>Share</b><br>{percent}%</div>', unsafe_allow_html=True)

    st.markdown("### 🍩 Market Share (Donut Chart)")
    fig = px.pie(names=summary.index, values=summary["Count"], hole=0.5)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📊 Comparison")
    st.bar_chart(summary["Count"])

# ======================
# 📝 SUBMIT
# ======================
elif page == "📝 Submit":

    st.title("📝 Add New Poll")

    age = st.selectbox("Age", AGE_GROUPS)
    region = st.selectbox("Region", REGIONS)
    option = st.selectbox("Option", OPTIONS)

    if st.button("Submit"):
        new = pd.DataFrame([{
            "Respondent_ID": len(df)+1,
            "Age": age,
            "Region": region,
            "Option": option,
            "Date": pd.Timestamp.now()
        }])

        df = pd.concat([df, new], ignore_index=True)
        save_data(df)

        st.success("✅ Submitted!")

# ======================
# 📊 ADVANCED ANALYSIS
# ======================
elif page == "📊 Advanced Analysis":

    st.title("📊 Deep Segment Analysis")

    col1, col2 = st.columns(2)

    region = col1.selectbox("Region", df["Region"].unique())
    age = col2.selectbox("Age", df["Age"].unique())

    filtered = df[(df["Region"] == region) & (df["Age"] == age)]

    if not filtered.empty:
        summary = calculate_summary(filtered)

        st.markdown("### 🎯 Segment Leader")
        leader = summary["Count"].idxmax()
        st.success(f"🏆 {leader} dominates in this segment")

        st.plotly_chart(px.bar(
            x=summary.index,
            y=summary["Count"],
            color=summary.index
        ), use_container_width=True)

# ======================
# 🌍 DEMOGRAPHICS
# ======================
elif page == "🌍 Demographics":

    st.title("🌍 Demographic Intelligence")

    region_df = region_analysis(df)

    st.markdown("### 🧠 Heatmap View")
    st.plotly_chart(px.imshow(region_df, text_auto=True), use_container_width=True)

    st.markdown("### 📊 Stacked % View")
    percent_df = region_df.div(region_df.sum(axis=1), axis=0)

    st.plotly_chart(px.bar(percent_df, barmode="stack"), use_container_width=True)

# ======================
# 📈 TRENDS
# ======================
elif page == "📈 Trends":

    st.title("📈 Growth & Trends")

    trend_df = trend_analysis(df)

    st.markdown("### 📊 Daily Trend")
    st.line_chart(trend_df.set_index("Date")["Responses"])

    st.markdown("### 📉 Moving Average")
    trend_df["MA"] = trend_df["Responses"].rolling(7).mean()
    st.line_chart(trend_df.set_index("Date")[["Responses", "MA"]])

# ======================
# 🏆 INSIGHTS LAB (🔥 UNIQUE PAGE)
# ======================
elif page == "🏆 Insights Lab":

    st.title("🏆 AI-like Insight Engine")

    summary = calculate_summary(df)

    top = summary["Count"].idxmax()
    lowest = summary["Count"].idxmin()

    st.success(f"🔥 {top} is dominating the market!")
    st.warning(f"⚠️ {lowest} is underperforming!")

    # Region leader
    region_df = region_analysis(df)

    st.markdown("### 🌍 Region Leaders")
    for region in region_df.index:
        leader = region_df.loc[region].idxmax()
        st.write(f"👉 {region}: {leader}")