# AI-Driven Predictive Maintenance Cost Forecasting System

An end-to-end industrial AI platform that predicts equipment degradation, estimates maintenance-related financial exposure, explains model predictions using Explainable AI (SHAP), generates executive insights using LLMs, and provides interactive analytics dashboards with automated PDF reporting.

---

# Project Overview

Industrial organizations often suffer from unexpected machine failures, leading to:

- Production downtime
- Revenue loss
- Emergency maintenance costs
- Inefficient maintenance scheduling
- Operational instability

This project builds a complete AI-powered Predictive Maintenance Intelligence System capable of:

- Predicting Remaining Useful Life (RUL)
- Forecasting failure probability
- Estimating financial maintenance exposure
- Explaining AI predictions using SHAP
- Generating executive insights using LLMs
- Providing interactive dashboards
- Automatically generating executive PDF reports

---

# Key Features

## Predictive Maintenance Modeling
- BiGRU-based deep learning architecture
- Remaining Useful Life (RUL) prediction
- Failure probability estimation
- Sequential time-series forecasting

## Financial Risk Forecasting
- Maintenance cost estimation
- Financial exposure analytics
- Monte Carlo simulation forecasting
- Risk distribution analysis

## Explainable AI (XAI)
- SHAP-based feature importance analysis
- Sensor contribution visualization
- Failure driver interpretation
- Transparent AI predictions

## AI Executive Intelligence
- Rule-based maintenance insights
- LLM-powered executive recommendations
- Automatic fallback system for LLM failures
- Human-readable maintenance intelligence

## Interactive Dashboard
Built using Streamlit with:
- Executive KPIs
- Financial analytics
- Risk visualizations
- SHAP explainability charts
- Monte Carlo simulation graphs
- Executive maintenance insights

## Automated PDF Reporting
Professional executive reports including:
- Asset risk analysis
- Financial forecasting
- SHAP explainability graphs
- Monte Carlo risk simulation
- AI-generated executive insights

---

# Tech Stack

## Programming Language
- Python

## Machine Learning & AI
- TensorFlow / Keras
- NumPy
- Pandas
- SHAP

## Data Visualization
- Plotly
- Matplotlib

## Dashboard Framework
- Streamlit

## Reporting
- FPDF

## LLM Integration
- Groq API
- Llama Models

---

# System Architecture

```text
Industrial Sensor Data
          ↓
Data Preprocessing
          ↓
BiGRU Deep Learning Model
          ↓
RUL Prediction + Failure Probability
          ↓
Financial Risk Forecasting
          ↓
SHAP Explainability Engine
          ↓
LLM Executive Intelligence
          ↓
Interactive Streamlit Dashboard
          ↓
Executive PDF Report Generation
```

---

# Dashboard Features

## Executive KPIs
- Total Assets
- High-Risk Assets
- Projected Financial Exposure
- Average Failure Probability

## Visual Analytics
- Maintenance Action Distribution
- Financial Exposure Distribution
- Monte Carlo Maintenance Forecasting
- Asset Financial Risk Mapping
- SHAP Failure Driver Analysis

## Executive Intelligence
- AI-generated maintenance recommendations
- Critical asset prioritization
- Operational risk interpretation
- Executive-level maintenance summaries

---

# Explainable AI (SHAP)

The project integrates SHAP Explainability to identify the most influential sensor variables contributing to industrial asset degradation and failure risk.

Benefits include:
- Transparent AI decisions
- Root-cause analysis
- Improved operational trust
- Better maintenance planning
- Interpretable industrial AI

---

# Monte Carlo Financial Simulation

Monte Carlo simulation is used to estimate uncertainty in future maintenance expenditure.

The simulation provides:
- Expected maintenance exposure
- Worst-case financial risk
- Best-case financial outcome
- Risk distribution forecasting

---

# LLM-Powered Executive Intelligence

The platform integrates Large Language Models (LLMs) to generate executive-level maintenance insights and operational recommendations.

Features:
- AI-generated maintenance recommendations
- Financial risk interpretation
- Executive operational summaries
- Automatic fallback to rule-based insights if LLM services fail

---

# Model Performance

## Final Optimized RMSE

```text
13.06
```

The BiGRU deep learning model achieved strong predictive performance for Remaining Useful Life (RUL) forecasting on industrial sensor data.

---

# Project Structure

```text
predictive-maintenance-intelligence-system/
│
├── dashboard/
│   └── app.py
│
├── utils/
│   └── report_generator.py
│
├── notebooks/
│
├── data/
│   └── processed/
│
├── reports/
│
├── models/
│
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/predictive-maintenance-intelligence-system.git
```

## Navigate to Project Directory

```bash
cd predictive-maintenance-intelligence-system
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Dashboard Screenshots

## Executive Dashboard
(Add Screenshot Here)

## SHAP Explainability
(Add Screenshot Here)

## Monte Carlo Risk Forecast
(Add Screenshot Here)

## Executive PDF Report
(Add Screenshot Here)

---

# Future Enhancements

- Real-time IoT sensor streaming
- Kafka/MQTT integration
- Digital Twin visualization
- Transformer-based forecasting models
- Cloud deployment (AWS / Azure / GCP)
- Docker containerization
- CI/CD pipelines
- Automated alert systems
- Enterprise role-based dashboards
- Predictive maintenance optimization engine

---

# Business Impact

The system enables industrial organizations to:

- Reduce unexpected downtime
- Improve maintenance scheduling
- Minimize operational losses
- Improve financial planning
- Increase operational efficiency
- Enable proactive maintenance decision-making

---

# Author

## Kartik Kumthe

Engineering Student | AI & Data Science Enthusiast

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

- TensorFlow
- Streamlit
- SHAP
- Plotly
- Groq API
- Open Source AI Community