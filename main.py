import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_parquet("transaction_fraud_data.parquet")

print("\n📊 Описание числовых колонок:")
print(df.describe())
print("\n📌 Распределение мошеннических транзакций:")
print(df['is_fraud'].value_counts(normalize=True))
categorical_cols = df.select_dtypes(include="object").columns
print("\n📦 Пример значения 'last_hour_activity':")
print(df['last_hour_activity'].iloc[0])
print("\n📎 Кол-во дубликатов по 'transaction_id':", df['transaction_id'].duplicated().sum())
print("\n🕒 Диапазон дат:")
print(df['timestamp'].min(), "→", df['timestamp'].max())
print("\n🌍 Процент транзакций вне страны клиента:")
print(df['is_outside_home_country'].value_counts(normalize=True))
