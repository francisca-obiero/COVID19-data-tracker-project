import pandas as pd

def clean_data(df, countries):
    df_filtered = df[df['location'].isin(countries)].copy()
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])
    
    # Drop rows missing critical values
    df_filtered = df_filtered.dropna(subset=['date', 'total_cases'])
    
    # Fill missing numeric values forward
    for col in ['total_cases', 'total_deaths', 'total_vaccinations']:
        if col in df_filtered.columns:
            df_filtered[col] = df_filtered[col].ffill()
    
    return df_filtered

if __name__ == "__main__":
    FILE_PATH = r"C:\Users\Admin\.cache\kagglehub\datasets\caesarmario\our-world-in-data-covid19-dataset\versions\432\owid-covid-data.csv"
    COUNTRIES = ['Kenya', 'USA', 'India']
    
    df = pd.read_csv(FILE_PATH)
    df_clean = clean_data(df, COUNTRIES)
    print(df_clean.head())
