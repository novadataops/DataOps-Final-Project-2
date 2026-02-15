import pandas as pd

def extract(file_path="data/raw_transactions.csv"):
    """Чтение CSV с сырыми данными"""
    df = pd.read_csv(file_path)
    print(f"[extract] Извлечено {len(df)} строк")
    return df
