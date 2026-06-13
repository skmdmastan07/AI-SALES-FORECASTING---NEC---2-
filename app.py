import streamlit as st

st.set_page_config(
    page_title="Intelligent Sales Forecasting System",
    page_icon="📈",
    layout="wide"
)

# =========================
# CUSTOM STYLING
# =========================

st.markdown("""
<style>

.hero-container{
    background: linear-gradient(
        135deg,
        #1e3c72,
        #2a5298,
        #2096f3
    );
    padding: 35px;
    border-radius: 20px;
    margin-bottom: 20px;
}

.feature-card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #374151;
    min-height:180px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero-container">
<h1 style="color:white;">
📈 Intelligent Sales Forecasting System
</h1>

<h4 style="color:white;">
AI-powered sales forecasting, inventory optimization,
and business intelligence platform
</h4>
</div>
""", unsafe_allow_html=True)

# =========================
# OVERVIEW
# =========================

st.subheader("🚀 Platform Overview")

st.write("""
This platform helps organizations analyze sales data,
forecast future demand, optimize inventory levels,
generate reports, and support data-driven decision making.
""")

st.divider()

# =========================
# FEATURE CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Analytics</h3>
        <br>
        Interactive charts, KPIs,
        category analysis,
        revenue trends,
        and business insights.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 Forecasting</h3>
        <br>
        Machine Learning based
        sales prediction using
        Linear Regression and
        Random Forest models.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>📦 Inventory</h3>
        <br>
        Inventory monitoring,
        safety stock calculation,
        reorder point analysis,
        and optimization.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# WORKFLOW
# =========================

st.subheader("⚡ Project Workflow")

workflow = [
    "Upload Sales Dataset",
    "Data Preprocessing",
    "Exploratory Data Analysis",
    "Model Training",
    "Sales Forecasting",
    "Inventory Optimization",
    "Reports Generation",
    "Executive Dashboard"
]

for i, step in enumerate(workflow, start=1):
    st.write(f"{i}. {step}")

st.success(
    "Use the sidebar to navigate through all project modules."
)