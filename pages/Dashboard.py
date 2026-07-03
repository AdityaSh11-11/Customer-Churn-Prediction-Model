import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("data.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.fillna(0, inplace=True)

st.title("Customer Churn Dashboard")

# ==========================
# KPI Cards
# ==========================

total = len(df)
churn = len(df[df["Churn"]=="Yes"])
retained = len(df[df["Churn"]=="No"])
rate = churn/total*100

c1,c2,c3,c4 = st.columns(4)

c1.metric("Customers", total)
c2.metric("Churned", churn)
c3.metric("Retained", retained)
c4.metric("Churn Rate", f"{rate:.2f}%")

st.divider()

# ==========================
# Charts
# ==========================

col1,col2 = st.columns(2)

fig = px.pie(
    df,
    names="Churn",
    title="Customer Churn Distribution",
    hole=.5
)

col1.plotly_chart(fig,use_container_width=True)

fig = px.histogram(
    df,
    x="MonthlyCharges",
    color="Churn",
    title="Monthly Charges Distribution"
)

col2.plotly_chart(fig,use_container_width=True)

col3,col4 = st.columns(2)

fig = px.box(
    df,
    x="Contract",
    y="MonthlyCharges",
    color="Churn",
    title="Contract vs Monthly Charges"
)

col3.plotly_chart(fig,use_container_width=True)

fig = px.histogram(
    df,
    x="tenure",
    color="Churn",
    title="Tenure Distribution"
)

col4.plotly_chart(fig,use_container_width=True)