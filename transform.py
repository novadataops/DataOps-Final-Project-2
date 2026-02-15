def transform(df):
    """Простейшая трансформация: суммируем расходы по категориям"""
    df['amount'] = df['amount'].astype(float)
    summary = df.groupby('category')['amount'].sum().reset_index()
    print("[transform] Трансформация завершена")
    return summary
