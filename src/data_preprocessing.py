import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Data loaded successfully!")
    print(df.head())
    return df

def clean_data(df):
    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    # Remove missing values
    df = df.dropna()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    print("Data cleaned successfully!")
    return df

if __name__ == "__main__":
    df = load_data("data/raw/walmart.csv")
    df = clean_data(df)
    print(df.info())