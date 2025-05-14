import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def explore_data(df):
    print("Columns in dataset:")
    print(df.columns)
    print("\nPreview of data:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    FILE_PATH = r"C:\Users\Admin\.cache\kagglehub\datasets\caesarmario\our-world-in-data-covid19-dataset\versions\432\owid-covid-data.csv"
    df = load_data(FILE_PATH)
    explore_data(df)
