import pandas as pd
import plotly.express as px

def plot_choropleth(df):
    latest_date = df['date'].max()
    df_latest = df[df['date'] == latest_date].dropna(subset=['iso_code', 'total_cases'])
    
    fig = px.choropleth(
        df_latest,
        locations='iso_code',
        color='total_cases',
        hover_name='location',
        color_continuous_scale='Reds',
        title=f'Global COVID-19 Total Cases as of {latest_date.date()}',
        labels={'total_cases': 'Total Cases'},
        projection='natural earth'  # Added projection for better map appearance
    )
    fig.update_geos(showcoastlines=True, coastlinecolor="RebeccaPurple")
    fig.show()

if __name__ == "__main__":
    FILE_PATH = r"C:\Users\Admin\.cache\kagglehub\datasets\caesarmario\our-world-in-data-covid19-dataset\versions\432\owid-covid-data.csv"
    df = pd.read_csv(FILE_PATH)
    df['date'] = pd.to_datetime(df['date'])
    plot_choropleth(df)
