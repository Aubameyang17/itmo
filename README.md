Было проведено базовое EDA по итогом которого выявлены следующие результаты:
Размер данных: (7483766, 23)
Типы данных и пропущенные значения:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7483766 entries, 0 to 7483765
Data columns (total 23 columns):
 #   Column                   Dtype         
---  ------                   -----         
 0   transaction_id           object        
 1   customer_id              object        
 2   card_number              int64         
 3   timestamp                datetime64[us]
 4   vendor_category          object        
 5   vendor_type              object        
 6   vendor                   object        
 7   amount                   float64       
 8   currency                 object        
 9   country                  object        
 10  city                     object        
 11  city_size                object        
 12  card_type                object        
 13  is_card_present          bool          
 14  device                   object        
 15  channel                  object        
 16  device_fingerprint       object        
 17  ip_address               object        
 18  is_outside_home_country  bool          
 19  is_high_risk_vendor      bool          
 20  is_weekend               bool          
 21  last_hour_activity       object        
 22  is_fraud                 bool          
dtypes: bool(5), datetime64[us](1), float64(1), int64(1), object(15)
Использование памяти: 1.0+ GB
Количество пропущенных значений по колонкам:
transaction_id             0
customer_id                0
card_number                0
timestamp                  0
vendor_category            0
vendor_type                0
vendor                     0
amount                     0
currency                   0
country                    0
city                       0
city_size                  0
card_type                  0
is_card_present            0
device                     0
channel                    0
device_fingerprint         0
ip_address                 0
is_outside_home_country    0
is_high_risk_vendor        0
is_weekend                 0
last_hour_activity         0
is_fraud                   0
dtype: int64
Описание числовых колонок:
        card_number                   timestamp        amount
count  7.483766e+06                     7483766  7.483766e+06
mean   4.222100e+15  2024-10-15 12:36:38.052469  4.792468e+04
min    3.700086e+14  2024-09-30 00:00:01.034820  1.000000e-02
25%    4.004400e+15  2024-10-07 18:08:27.325326  3.635300e+02
50%    5.010745e+15  2024-10-15 12:46:31.739295  1.177450e+03
75%    5.999914e+15  2024-10-23 07:37:00.969509  2.242953e+04
max    6.999728e+15  2024-10-30 23:59:59.101885  6.253153e+06
std    2.341170e+15                         NaN  1.775562e+05
Распределение мошеннических транзакций:
is_fraud
False    0.800272
True     0.199728
Диапазон дат:
2024-09-30 00:00:01.034820 → 2024-10-30 23:59:59.101885
Был построен график частоты использования разных банковских карт что покажет компании какие сейчас тренды, что нужно лучше развивать, а что уже в топе (выяснилось что самый популярный тип карты Basic Debit, а не популярный Basic Credit)
