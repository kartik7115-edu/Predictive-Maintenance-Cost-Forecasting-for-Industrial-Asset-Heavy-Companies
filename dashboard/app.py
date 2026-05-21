import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import sys
from pathlib import Path

st.set_page_config(

    page_title="Predictive Maintenance Financial Dashboard",

    layout="wide"
)

st.title("AI-Driven Predictive Maintenance Cost Forecasting")

st.markdown(
    "Industrial Asset Health & Financial Risk Analytics"
)

BASE_DIR = Path(__file__).resolve().parent.parent

results_df = pd.read_csv(
    BASE_DIR / "data/processed/maintenance_predictions.csv"
)

simulation_df = pd.read_csv(
    BASE_DIR / "data/processed/monte_carlo_results.csv"
)

shap_df = pd.read_csv(
    BASE_DIR / "data/processed/shap_feature_importance.csv"
)

insights_df = pd.read_csv(
    BASE_DIR / "data/processed/final_dashboard_data.csv"
)

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(ROOT_DIR)
)

from utils.report_generator import generate_executive_report


total_assets = len(results_df)

high_risk_assets = len(
    results_df[
        results_df['Maintenance_Action']
        == "Immediate Maintenance"
    ]
)

total_exposure = results_df[
    'Total_Financial_Impact'
].sum()

avg_risk = results_df[
    'Failure_Probability'
].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Assets",
    total_assets
)

col2.metric(
    "High Risk Assets",
    high_risk_assets
)

col3.metric(
    "Projected Exposure",
    f"Rs. {total_exposure:,.0f}"
)

col4.metric(
    "Average Failure Risk",
    f"{avg_risk:.2%}"
)

action_counts = results_df[
    'Maintenance_Action'
].value_counts().reset_index()

action_counts.columns = [
    'Action',
    'Count'
]

fig1 = px.bar(

    action_counts,

    x='Action',
    y='Count',

    title="Maintenance Action Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

financial_summary = results_df.groupby(
    'Maintenance_Action'
)[
    'Total_Financial_Impact'
].sum().reset_index()

fig2 = px.pie(

    financial_summary,

    names='Maintenance_Action',
    values='Total_Financial_Impact',

    title="Financial Exposure Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(

    simulation_df,

    x='Simulated_Total_Cost',

    nbins=50,

    title="Monte Carlo Maintenance Cost Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Asset Risk Overview")

st.dataframe(

    results_df[[
        'Predicted_RUL',
        'Maintenance_Action',
        'Failure_Probability',
        'Total_Financial_Impact'
    ]].head(50)
)

fig4 = px.scatter(

    results_df,

    x='Predicted_RUL',
    y='Total_Financial_Impact',

    color='Maintenance_Action',

    title="Asset Financial Risk Map"
)

st.plotly_chart(fig4, use_container_width=True)

mean_cost = simulation_df[
    'Simulated_Total_Cost'
].mean()

p95 = simulation_df[
    'Simulated_Total_Cost'
].quantile(0.95)

st.subheader("Financial Risk Forecast")

st.write(
    f"Expected Maintenance Exposure: Rs. {mean_cost:,.0f}"
)

st.write(
    f"95th Percentile Risk Exposure: Rs. {p95:,.0f}"
)

st.subheader("Top Failure Drivers")

fig5 = px.bar(

    shap_df.sort_values(
        by='Importance',
        ascending=True
    ),

    x='Importance',
    y='Feature',

    orientation='h',

    title="Most Influential Sensors in Failure Prediction"
)

fig5.update_traces(
    marker_color='crimson'
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

top_sensor = shap_df.iloc[0]['Feature']

st.info(

    f"""
    The predictive model identifies
    {top_sensor}
    as the strongest contributor to
    industrial asset degradation risk.

    High variability in this sensor
    strongly correlates with reduced
    Remaining Useful Life (RUL) and
    increased maintenance exposure.
    """
)

# ---------- LLM Integration

insight_mode = st.sidebar.selectbox(

    "Insight Engine",

    [
        "Rule-Based",
        "LLM-Powered"
    ]
)

if insight_mode == "Rule-Based":

    insight_column = "Rule_Based_Insight"

else:

    insight_column = "LLM_Insight"

top_assets = insights_df.nlargest(

    10,

    'Total_Financial_Impact'
)

st.subheader("Executive Insights: Highest Risk Assets")

for idx, row in top_assets.iterrows():

    st.info(

        f"""
        Asset ID: {idx}

        Predicted RUL:
        {row['Predicted_RUL']:.1f}

        Failure Probability:
        {row['Failure_Probability']:.2f}

        Financial Exposure:
        Rs.{row['Total_Financial_Impact']:,.0f}

        Insight:
        {row[insight_column]}
        """
    )

st.header(
    "Executive Report Generation"
)

simulation_totals = simulation_df[
    'Simulated_Total_Cost'
].values

if st.button(
    "Generate Executive PDF Report"
):

    results_df['LLM_Insight'] = insights_df['LLM_Insight']

    results_df['Rule_Based_Insight'] = insights_df['Rule_Based_Insight']

    report_path = generate_executive_report(

        results_df,

        shap_df,

        simulation_totals
    )

    st.success(
        "Executive Report Generated Successfully!"
    )

    with open(report_path, "rb") as pdf_file:

        st.download_button(

            label="Download Executive Report",

            data=pdf_file,

            file_name="executive_report.pdf",

            mime="application/pdf"
        )