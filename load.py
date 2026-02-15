def load(df, output_path="data/processed_transactions.csv"):
    """Сохраняем обработанные данные"""
    df.to_csv(output_path, index=False)
    print(f"[load] Загружено {len(df)} строк в {output_path}")
