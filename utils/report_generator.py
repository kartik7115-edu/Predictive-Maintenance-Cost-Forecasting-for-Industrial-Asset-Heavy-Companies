# =========================================================
from fpdf import FPDF
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


def generate_executive_report(
    results_df,
    importance_df,
    simulation_totals
    ):

    simulation_totals = np.array(simulation_totals)

    # =====================================================
    # CREATE REPORTS FOLDER
    # =====================================================

    REPORT_DIR = os.path.join(
        os.path.dirname(__file__),
        "..",
        "reports"
    )

    os.makedirs(REPORT_DIR, exist_ok=True)

    # =====================================================
    # CREATE ASSET IDS
    # =====================================================

    results_df['Asset_ID'] = [

        f"AST-{1000+i}"

        for i in range(len(results_df))
    ]

    # =====================================================
    # CREATE RISK LEVELS
    # =====================================================

    def risk_level(prob):

        if prob > 0.85:

            return "CRITICAL"

        elif prob > 0.60:

            return "HIGH"

        elif prob > 0.40:

            return "MODERATE"

        else:

            return "LOW"

    results_df['Risk_Level'] = results_df[
        'Failure_Probability'
    ].apply(risk_level)

    # =====================================================
    # TOP ASSETS GRAPH
    # =====================================================

    top_assets_chart = results_df.nlargest(

        10,

        'Total_Financial_Impact'
    )

    plt.figure(figsize=(8,5))

    plt.bar(

        top_assets_chart['Asset_ID'],

        top_assets_chart['Total_Financial_Impact']
    )

    plt.xlabel("Asset ID")

    plt.ylabel("Financial Exposure")

    plt.title("Top Critical Assets")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORT_DIR, "top_assets.png")
    )

    plt.close()

    # =====================================================
    # SHAP GRAPH
    # =====================================================

    top_shap = importance_df.head(10)

    plt.figure(figsize=(8,5))

    plt.barh(

        top_shap['Feature'],

        top_shap['Importance']
    )

    plt.xlabel("Importance")

    plt.ylabel("Feature")

    plt.title("Top Failure Drivers")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORT_DIR, "shap_importance.png")
    )

    plt.close()

    # =====================================================
    # MONTE CARLO GRAPH
    # =====================================================

    plt.figure(figsize=(8,5))

    plt.hist(

        simulation_totals,

        bins=30
    )

    plt.xlabel("Forecasted Maintenance Cost")

    plt.ylabel("Frequency")

    plt.title(
        "Monte Carlo Maintenance Cost Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORT_DIR, "monte_carlo.png")
    )

    plt.close()

    # =====================================================
    # CREATE PDF
    # =====================================================

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.add_page()

    # =====================================================
    # TITLE
    # =====================================================

    pdf.set_font(
        "Arial",
        style='B',
        size=20
    )

    pdf.cell(

        200,

        10,

        txt="Predictive Maintenance Executive Report",

        ln=True,

        align='C'
    )

    pdf.ln(10)

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    total_assets = len(results_df)

    high_risk_assets = len(

        results_df[
            results_df['Failure_Probability'] > 0.7
        ]
    )

    total_exposure = results_df[
        'Total_Financial_Impact'
    ].sum()

    pdf.set_font(
        "Arial",
        style='B',
        size=16
    )

    pdf.cell(

        200,

        10,

        txt="Executive Summary",

        ln=True
    )

    pdf.set_font(
        "Arial",
        size=12
    )

    summary_text = f"""

    Total Assets Monitored:
    {total_assets}

    High-Risk Assets:
    {high_risk_assets}

    Projected Financial Exposure:
    Rs. {total_exposure:,.0f}
    """
    summary_text = summary_text.replace("₹", "Rs.")

    pdf.multi_cell(
        0,
        8,
        summary_text
    )

    pdf.ln(5)

    # =====================================================
    # TOP CRITICAL ASSETS
    # =====================================================

    pdf.set_font(
        "Arial",
        style='B',
        size=16
    )

    pdf.cell(

        200,

        10,

        txt="Top Critical Assets",

        ln=True
    )

    pdf.image(

        os.path.join(REPORT_DIR, "top_assets.png"),

        x=20,

        w=160
    )

    pdf.ln(10)

    top_assets = results_df.nlargest(

        5,

        'Total_Financial_Impact'
    )

    pdf.set_font(
        "Arial",
        size=11
    )

    for _, row in top_assets.iterrows():

        asset_text = f"""

    Asset ID:
    {row['Asset_ID']}

    Risk Level:
    {row['Risk_Level']}

    Predicted RUL:
    {row['Predicted_RUL']:.1f}

    Failure Probability:
    {row['Failure_Probability']:.2f}

    Financial Exposure:
    Rs. {row['Total_Financial_Impact']:,.0f}

    Recommended Action:
    {row['Maintenance_Action']}
    """
        asset_text = asset_text.replace("₹", "Rs.")
        pdf.multi_cell(
            0,
            7,
            asset_text
        )

        pdf.ln(2)

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    pdf.set_font(
        "Arial",
        style='B',
        size=16
    )

    pdf.cell(

        200,

        10,

        txt="AI Executive Insights",

        ln=True
    )

    pdf.set_font(
        "Arial",
        size=11
    )

    for _, row in top_assets.iterrows():

        clean_insight = str(row['LLM_Insight']).replace("₹", "Rs.")
        insight_text = f"""

    Asset ID:
    {row['Asset_ID']}

    
    {clean_insight}
    """

        pdf.multi_cell(
            0,
            7,
            insight_text
        )

        pdf.ln(3)

    # =====================================================
    # SHAP FAILURE DRIVERS
    # =====================================================

    pdf.set_font(
        "Arial",
        style='B',
        size=16
    )

    pdf.cell(

        200,

        10,

        txt="Top Failure Drivers",

        ln=True
    )

    pdf.image(

        os.path.join(REPORT_DIR, "shap_importance.png"),

        x=20,

        w=160
    )

    pdf.ln(10)

    # =====================================================
    # MONTE CARLO FORECAST
    # =====================================================

    pdf.set_font(
        "Arial",
        style='B',
        size=16
    )

    pdf.cell(

        200,

        10,

        txt="Monte Carlo Risk Forecast",

        ln=True
    )

    pdf.image(

        os.path.join(REPORT_DIR, "monte_carlo.png"),

        x=20,

        w=160
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        size=11
    )

    mean_cost = np.mean(simulation_totals)

    max_cost = np.max(simulation_totals)

    min_cost = np.min(simulation_totals)

    mc_text = f"""

    Average Forecasted Maintenance Cost:
    Rs. {mean_cost:,.0f}

    Worst-Case Maintenance Exposure:
    Rs. {max_cost:,.0f}

    Best-Case Maintenance Exposure:
    Rs. {min_cost:,.0f}
    """
    mc_text = mc_text.replace("₹", "Rs.")
    pdf.multi_cell(
        0,
        8,
        mc_text
    )

    # =====================================================
    # CONCLUSION
    # =====================================================

    pdf.set_font(
        "Arial",
        style='B',
        size=16
    )

    pdf.cell(

        200,

        10,

        txt="Conclusion",

        ln=True
    )

    pdf.set_font(
        "Arial",
        size=11
    )

    conclusion_text = """

    The AI-powered predictive maintenance
    platform combines machine learning,
    financial forecasting, explainable AI,
    and executive intelligence to identify
    operational risk and forecast
    maintenance-related financial exposure.
    """

    pdf.multi_cell(
        0,
        8,
        conclusion_text
    )

    # =====================================================
    # FOOTER
    # =====================================================

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        style='I',
        size=10
    )

    footer_text = f"""

    Report Generated By:
    Industrial Decision Intelligence System built by KARTIK

    Generated On:
    {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
    """

    pdf.multi_cell(
        0,
        6,
        footer_text
    )

    # =====================================================
    # EXPORT PDF
    # =====================================================

    report_path = os.path.join(
        REPORT_DIR,
        "executive_report.pdf"
    )

    pdf.output(report_path)

    return report_path