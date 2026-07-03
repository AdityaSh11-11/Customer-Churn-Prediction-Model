import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)
plot_template = "plotly_white"

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("data.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")
df.fillna(0,inplace=True)

st.title("Customer Churn Analytics Dashboard")

# Sidebar Filters

contract = st.sidebar.multiselect(
    "Contract",
    df["Contract"].unique(),
    default=df["Contract"].unique()
)

internet = st.sidebar.multiselect(
    "Internet",
    df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

filtered = df[
    (df["Contract"].isin(contract)) &
    (df["InternetService"].isin(internet)) &
    (df["gender"].isin(gender))
]

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        len(filtered)
    )

with col2:
    churn_rate = filtered["Churn"].value_counts(normalize=True).get("Yes",0)*100

    st.metric(
        "Churn Rate",
        f"{churn_rate:.1f}%"
    )

with col3:
    st.metric(
        "Average Monthly Charges",
        f"${filtered['MonthlyCharges'].mean():.2f}"
    )

with col4:
    st.metric(
        "Average Tenure",
        f"{filtered['tenure'].mean():.1f} Months"
    )

st.subheader("Customer Churn by Contract Type")

fig = px.histogram(
    filtered,
    title="Customer Churn by Contract Type",
    x="Contract",
    color="Churn",
    barmode="group",
    color_discrete_sequence=["#4CAF50","#EF5350"],
    template=plot_template,
    labels={
        "Contract":"Contract Type",
        "count":"Customers",
        "Churn":"Churn Status"
    }
)

fig.update_layout(
    height=500,
    title="",
    title_x=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("Customer Distribution")

fig = px.sunburst(
    filtered,
    title="Customer Distribution by Internet Service, Contract Type and Churn Status",
    path=["InternetService","Contract","Churn"],
    color="Churn",
    color_discrete_map={
        "Yes":"#EF5350",
        "No":"#4CAF50"
    },
    template=plot_template
)

fig.update_layout(
    height=650,
    title="",
    title_x=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Average Monthly Charges by Churn Status")

avg = (
    filtered.groupby("Churn", as_index=False)["MonthlyCharges"]
    .mean()
)

fig = px.bar(
    avg,
    title="Average Monthly Charges by Churn Status",
    x="Churn",
    y="MonthlyCharges",
    color="Churn",
    text_auto=True,
    labels={
        "Churn":"Churn Status",
        "MonthlyCharges":"Average Monthly Charges ($)"
    },
    color_discrete_map={
        "Yes":"#EF5350",
        "No":"#22C55E"
    },
    template="plotly_white"
)

fig.update_layout(
    height=550,
    title_x=0.5,
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="monthly_charge"
)

st.subheader("Correlation Heatmap")

corr = filtered.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    title="Correlation Heatmap",
    text_auto=True,
    color_continuous_scale="RdBu_r",
    template=plot_template
)

fig.update_layout(
    height=650,
    title_x=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Top 10 Features Influencing Customer Churn")

with open("customer_churn_model.pkl","rb") as f:
    saved = pickle.load(f)

model = saved["model"]
features = saved["features_names"]

importance = model.feature_importances_

imp = pd.DataFrame({
    "Feature":features,
    "Importance":importance
})

imp = imp.sort_values(
    "Importance",
    ascending=False
)

fig = px.bar(
    imp.head(10),
    title="Top 10 Features Influencing Customer Churn",
    x="Importance",
    y="Feature",
    orientation="h",
    text="Importance",
    color="Importance",
    color_continuous_scale="Viridis",
    template=plot_template
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig.update_layout(
    height=550,
    title_x=0.5,
    coloraxis_showscale=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)