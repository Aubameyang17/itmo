import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Без GUI
import matplotlib.pyplot as plt
import os

# Загружаем данные
df = pd.read_parquet("transaction_fraud_data.parquet")

# Создаем директорию для графиков
os.makedirs("eda_charts", exist_ok=True)

# 1. Распределение суммы транзакций (лог-шкала)
plt.figure(figsize=(10, 6))
sns.histplot(df['amount'], bins=50, kde=True)
plt.xscale('log')
plt.title("Распределение суммы транзакций (логарифмическая шкала)")
plt.xlabel("Сумма транзакции")
plt.ylabel("Количество")
plt.tight_layout()
plt.savefig("eda_charts/amount_distribution.png")
plt.close()

# 2. Количество транзакций по типу карты
plt.figure(figsize=(8, 5))
sns.countplot(data=df, y="card_type", order=df['card_type'].value_counts().index)
plt.title("Частота использования типов карт")
plt.xlabel("Количество транзакций")
plt.ylabel("Тип карты")
plt.tight_layout()
plt.savefig("eda_charts/card_type_frequency.png")
plt.close()

# 3. Доля мошеннических транзакций
plt.figure(figsize=(6, 4))
fraud_counts = df['is_fraud'].value_counts()
fraud_counts.plot(kind='pie', autopct='%1.1f%%', labels=["Не мошенничество", "Мошенничество"], startangle=90)
plt.title("Распределение мошеннических транзакций")
plt.ylabel("")
plt.tight_layout()
plt.savefig("eda_charts/fraud_pie_chart.png")
plt.close()

print("✅ Графики успешно сохранены в папку 'eda_charts'")
