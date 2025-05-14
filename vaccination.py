import pandas as pd
import matplotlib.pyplot as plt

def plot_vaccinations(df, countries):
    plt.figure(figsize=(12,6))
    for country in countries:
        country_data = df[df['location'] == country].sort_values('date')
        # Forward fill missing total_vaccinations if any
        country_data['total_vaccinations'] = country_data['total_vaccinations'].ffill()
        plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
    plt.title('COVID-19 Vaccinations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
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
    
    plot_vaccinations(df, COUNTRIES)
