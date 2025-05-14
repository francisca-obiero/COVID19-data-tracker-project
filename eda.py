import pandas as pd
import matplotlib.pyplot as plt

def plot_total_cases(df, countries):
    plt.figure(figsize=(12,6))
    for country in countries:
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_cases'], label=country)
    plt.title('Total COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_total_deaths(df, countries):
    plt.figure(figsize=(12,6))
    for country in countries:
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_deaths'], label=country)
    plt.title('Total COVID-19 Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    FILE_PATH = r"C:\Users\Admin\.cache\kagglehub\datasets\caesarmario\our-world-in-data-covid19-dataset\versions\432\owid-covid-data.csv"
    COUNTRIES = ['Kenya', 'USA', 'India']
    
    df = pd.read_csv(FILE_PATH)
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['location'].isin(COUNTRIES)]
    
    plot_total_cases(df, COUNTRIES)
    plot_total_deaths(df, COUNTRIES)
