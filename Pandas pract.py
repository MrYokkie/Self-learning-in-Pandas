import pandas as pd
import matplotlib as plt
data = pd.read_csv("IPG2211A2N.csv")
print(data.head(n=15))
print(data)
data.columns
Index(data['observation_date', 'IPG2211A2N'], dtype='object')
plt.plot(data['observation_date'], data['IPG2211A2N'])

plt.plot(data['observation_date'], data['IPG2211A2N'])
plt.plot(data['observation_date'], data['IPG2211A2N'].rolling(100).mean())

plt.plot(data['observation_date'], data['IPG2211A2N'])
plt.plot(data['observation_date'], [data['IPG2211A2N'].mean()]*len(data))
# Данные даны за слишком длительный период - очень большой участок не актуален, среднний, максимальный, минимальный показатель нам ни о чем не говорит
first_date = pd.Timestamp(year=2015, month=1, day=1)
data2 = data[data['observation_date'] > first_date]
plt.plot(data2['observation_date'], data2['IPG2211A2N'])
plt.plot(data2['observation_date'], [data2['IPG2211A2N'].mean()]*len(data2))
from sklearn.linear_model import LinearRegression
N = len(data2)
x_range = pd.DataFrame(list(range(N)))
# x_range
regressor = LinearRegression()
regressor.fit(x_range, data2['IPG2211A2N'])
result = regressor.predict(x_range)
len(result)
len(data2['observation_date'])
plt.plot(x_range.index, data2['IPG2211A2N'])
plt.plot(x_range.index, result)
quant_95 = [data2['IPG2211A2N'].quantile(0.95)] * N
quant_05 = [data2['IPG2211A2N'].quantile(0.05)] * N
# Коридор, в который попадает 90% значений
plt.plot(data2['observation_date'], data2['IPG2211A2N'])
plt.plot(data2['observation_date'], [data2['IPG2211A2N'].mean()]*len(data2))
plt.plot(data2['observation_date'], quant_95)
plt.plot(data2['observation_date'], quant_05)
# Автокорреляция: смотрим сезонность
# График сезонности за последние 5 лет: ярко выражена годовая и полугодовая сезонность
plt.figure(figsize=(20, 5))
pd.plotting.autocorrelation_plot(data2['IPG2211A2N'])
plt.locator_params(axis='x', nbins=50)

# График автокорреляции для всех данных с 1940 года: ничего нельзя сказать о сезонности
plt.figure(figsize=(20, 5))
pd.plotting.autocorrelation_plot(data['IPG2211A2N'])
plt.locator_params(axis='x', nbins=50)

# 1) Из рассмотренных методов к данным о производстве газа применим тренд
# 2) Очень большой отрезок данных нерелевантен (как минимум до 2010 года стоило отбросить данные)
# 3) После 2015 года наблюдвается ярко выраженная полугодовая сезонность в данных
# 4) После 2015 года имеет смысл исследовать вероятностный диапазон значений, среднее и т.п. характеристики, для всего датасета результат этих функций не имеет смысла

print('Минимум с 2015 по 2020 год:', data['IPG2211A2N'].min())
print('Максимум с 2015 по 2020 год:', data['IPG2211A2N'].max())
print('Среднее с 2015 по 2020 год:', data['IPG2211A2N'].mean())

# Модели для предсказания сезонности: ARIMA, (ARMA, AMA, SARIMA, SARIMAX, garch)