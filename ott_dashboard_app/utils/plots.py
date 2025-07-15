
import plotly.express as px
import streamlit as st

def overview_charts(df):
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(df, names="platform", title="Content Share by Platform")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        year_df = df[df["release_year"].notna()]
        fig = px.area(year_df, x="release_year", title="Content Release Over Time", color="platform")
        st.plotly_chart(fig, use_container_width=True)

def country_analysis(df):
    country_count = df["country"].value_counts().reset_index()
    country_count.columns = ["country", "count"]
    fig = px.choropleth(country_count, locations="country", locationmode="country names",
                        color="count", title="Content Count by Country")
    st.plotly_chart(fig, use_container_width=True)

def chart_race(df):
    df = df[df["release_year"].notna()]
    grouped = df.groupby(["release_year", "listed_in"]).size().reset_index(name='count')
    fig = px.bar(grouped.sort_values(by="count", ascending=False).head(10),
                 x='listed_in', y='count', color='listed_in', animation_frame='release_year',
                 title="Top Genres Over Time")
    st.plotly_chart(fig, use_container_width=True)

def business_insights(df):
    genre_count = df["listed_in"].value_counts().head(10).reset_index()
    genre_count.columns = ["Genre", "Count"]
    st.bar_chart(genre_count.set_index("Genre"))
