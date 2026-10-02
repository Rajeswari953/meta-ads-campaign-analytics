# Meta Ads Campaign Analytics

An interactive dashboard for analyzing **Facebook and Instagram advertising campaign performance** using Python, Pandas, Plotly, and Streamlit.

## 📌 Problem Statement

Meta advertising campaigns generate multiple performance metrics such as:

- Spend
- Impressions
- Reach
- Clicks
- CTR
- CPC
- CPM
- Conversions
- Leads
- Cost per Conversion
- Cost per Lead

When these metrics are available as raw campaign-level data, it can be difficult to quickly understand **which campaigns and platforms are performing differently, where advertising spend is going, and how efficiently campaigns are generating clicks, leads, and conversions**.

A structured dashboard is needed to transform raw advertising data into an interactive and easy-to-understand performance view.

## 💡 Solution

This project provides an interactive **Meta Ads Campaign Performance Dashboard** that converts campaign data into visual business insights.

The dashboard allows users to:

- Filter campaigns by date range
- Compare different campaigns
- Compare Facebook and Instagram performance
- Monitor advertising spend and delivery metrics
- Evaluate click and conversion performance
- Review CTR, CPC, and cost per conversion
- Identify campaigns with comparatively higher or lower performance
- Understand campaign-level and platform-level differences through visualizations

## 🎯 Project Objective

The main objective is to build a simple analytics solution that helps users move from **raw Meta Ads campaign data → structured metrics → visual performance insights**.

## 📊 Dashboard Features

### KPI Overview

The dashboard provides key performance indicators including:

- **Total Spend**
- **Impressions**
- **Clicks**
- **Conversions**
- **CTR**
- **CPC**
- **Leads**
- **Cost per Conversion**

### Performance Analytics

The dashboard includes:

- Daily Ad Spend trend
- Conversion distribution
- Spend by Campaign
- Conversions by Campaign
- CTR comparison across platforms
- Cost per Conversion comparison across platforms

### Interactive Filters

Users can filter the dashboard using:

- Date Range
- Campaign
- Platform

## 🔄 Data Workflow

```text
Raw Meta Ads Data
        ↓
Data Loading
        ↓
Data Cleaning & Preparation
        ↓
Metric Processing
        ↓
Campaign & Platform Aggregation
        ↓
Interactive Visualizations
        ↓
Business Insights
```

## 🛠️ Technologies Used

- **Python** – Data processing and application development
- **Pandas** – Data cleaning, transformation, and aggregation
- **NumPy** – Numerical processing
- **Plotly** – Interactive charts and visualizations
- **Streamlit** – Interactive dashboard development
- **CSV** – Dataset storage
- **Git & GitHub** – Version control and project hosting

## 📁 Project Structure

```text
meta-ads-campaign-analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── DATA_DICTIONARY.md
│
└── data/
    └── meta_ads_sample.csv
```

## 📌 Dataset

The dashboard uses a structured Meta Ads campaign dataset containing fields such as:

- Date
- Campaign
- Ad Set
- Platform
- Spend
- Impressions
- Reach
- Clicks
- Conversions
- Leads
- CTR
- CPC
- CPM
- Conversion Rate
- Cost per Conversion
- Cost per Lead

The dataset used in this portfolio project is **sample/synthetic data** created for demonstration purposes. It does not contain confidential Zippy Digital Solutions or client campaign data.

## 💼 Internship Connection

This portfolio project was developed based on the skills and concepts practiced during my internship as a **Meta Ads Analyst Intern at Zippy Digital Solutions, Madurai**.

During the internship, I worked with Facebook and Instagram advertising campaign data and learned how campaign metrics such as spend, impressions, reach, clicks, CTR, CPC, CPM, conversions, and leads can be used to evaluate advertising performance.

This GitHub project is an **independent portfolio implementation** created to demonstrate those skills. It is not an official Zippy Digital Solutions project and does not use confidential company or client data.

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rajeswari953/meta-ads-campaign-analytics.git
```

### 2. Open the project folder

```bash
cd meta-ads-campaign-analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 📈 Business Value

This dashboard demonstrates how advertising data can be transformed into a practical reporting solution.

It can help users:

- Understand advertising spend distribution
- Compare campaign performance
- Compare platform-level results
- Review acquisition efficiency
- Identify areas that require further campaign review
- Present advertising performance through an interactive dashboard

## 🔮 Future Improvements

Possible future improvements include:

- Connecting the dashboard to live Meta Ads API data
- Adding campaign-level trend comparisons
- Adding creative-level performance analysis
- Adding audience-level breakdowns
- Adding automated reporting
- Connecting the dashboard to a database instead of CSV files

