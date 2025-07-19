import pandas as pd

# Загружаем транзакции
df = pd.read_parquet("transaction_fraud_data.parquet")

# Извлекаем вложенное поле 'unique_merchants' из last_hour_activity
df['unique_merchants'] = df['last_hour_activity'].apply(lambda x: x['unique_merchants'])

# Группируем по клиенту и считаем медиану unique_merchants
medians = df.groupby('customer_id')['unique_merchants'].median()

# Находим 95-й квантиль среди этих медиан
quantile_95 = medians.quantile(0.95)

# Считаем количество клиентов с медианой строго выше 95-го квантили
suspicious_clients_count = (medians > quantile_95).sum()

print(suspicious_clients_count)
