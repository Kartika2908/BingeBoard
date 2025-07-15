import streamlit as st
import pandas as pd
import plotly.express as px
from utils import plots, pdf_export, helpers
from datetime import datetime

st.set_page_config(page_title="OTT Platform Insights", layout="wide")

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-image: url("assets/sidebar_bg.jpg");
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)

df_netflix = pd.read_csv("data/netflix_titles.csv")
df_prime = pd.read_csv("data/amazon_prime_titles.csv")
df_disney = pd.read_csv("data/disney_plus_titles.csv")

df = helpers.clean_and_merge([df_netflix, df_prime, df_disney])

with st.sidebar:
    st.title("Binge Board")
    selected_platform = st.multiselect("Platform", df["platform"].unique(), default=df["platform"].unique())
    selected_country = st.multiselect("Country", df["country"].dropna().unique())
    selected_genre = st.multiselect("Genre", df["listed_in"].dropna().unique())

df_filtered = helpers.filter_data(df, selected_platform, selected_country, selected_genre)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Overview", "🌍 Country Analysis", "🏁 Chart Race", "📤 Export", "💡 Business Insights", "📨 Contact"
])

with tab1:
    st.header("OTT Content Overview")
    plots.overview_charts(df_filtered)

with tab2:
    st.header("Country-wise Analysis")
    plots.country_analysis(df_filtered)

with tab3:
    st.header("Top Genres Over Time")
    plots.chart_race(df_filtered)

with tab4:
    st.header("Export Reports")
    csv = helpers.convert_df_to_csv(df_filtered)
    st.download_button("Download Filtered Data (CSV)", csv, "filtered_ott.csv", "text/csv")
    if st.button("Generate PDF Report"):
        pdf_export.generate_pdf(df_filtered)
        with open("OTT_Report.pdf", "rb") as f:
            st.download_button("Download PDF Report", f, "OTT_Report.pdf", "application/pdf")

with tab5:
    st.header("Business Insights")
    plots.business_insights(df_filtered)

with tab6:
    st.header("📨 Contact Form")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            helpers.save_contact(name, email, message)
            st.success("Thank you! We’ll get in touch.")
