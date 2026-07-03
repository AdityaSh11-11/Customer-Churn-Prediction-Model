import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction System",
    page_icon="📊",
    layout="wide"
)

# Load CSS
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(f"""
<div style="
position:relative;
background:linear-gradient(135deg,#145680,#7c3aed);
padding:10px;
border-radius:30px;
margin-bottom:30px;
margin-top:20px;
text-align:center;
">

<!-- Title -->
<h1 style="
font-size:58px;
font-weight:700;
color:white;
margin-bottom:0;
padding-bottom:0;
">

Customer Churn Prediction System

</h1>
<h2 style="
font-size:22px;
color:#dbeafe;
margin-top:0px;
">

Predict customer churn, uncover insights and drive smarter retention strategies.

</h2>

</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.2,1])

with right:

    st.markdown("""
<div class="about-container">

<div class="about-title">
About the System
</div>

<div class="about-text">

<ul>

<li>The Customer Churn Prediction System is a machine learning-based web application developed to identify customers who are likely to discontinue a company's services.</li>

<li>It helps businesses analyze customer behavior and make proactive decisions to reduce customer attrition.</li>

<li>The application is built using Python, Machine Learning, and Streamlit.</li>
<li>Overall, this project combines data preprocessing, machine learning, interactive visualization, and business intelligence to support data-driven decision-making in customer relationship management.</li>

</ul>

</div>

</div>
""", unsafe_allow_html=True)


    if st.button("Prediction", use_container_width=True):
        st.switch_page("pages/Prediction.py")

    if st.button("Analytics", use_container_width=True):
        st.switch_page("pages/Analytics.py")

    if st.button("Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

with left:

    st.image("assets/logo.png", use_container_width=True)

st.divider()

st.markdown(
"""
<h2 style='text-align:center;color:white;'>
Customer Churn Prediction
</h2>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p style='text-align:center;color:#cbd5e1;font-size:18px;'>
© 2025 Customer Churn Prediction System | Built by Aditya Sharma | All rights reserved.

</p>
""",
unsafe_allow_html=True
)
