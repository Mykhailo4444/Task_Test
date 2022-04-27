# task 4
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 999999)
pd.set_option('display.max_columns', 999999)
pd.set_option('display.width', 999999)

# file = open("weather_dataset.data.txt", 'r')
# deleter = lambda x: " ".join(x.split())
# tmp_lst = [deleter(i) for i in file.readlines()]
# file.close()
#
# file = open("weather.txt", 'w')
# for line in tmp_lst:
#     file.write(line + '\n')
# file.close()

data = pd.read_csv("weather.txt", sep=" ", header=0)


data['Yr'] = '19' + data['Yr'].astype(str)
data['Mo'] = data['Mo'].astype(str).apply(lambda x: '0' + x if len(x) == 1 else x)
data['Dy'] = data['Dy'].astype(str).apply(lambda x: '0' + x if len(x) == 1 else x)
data['Date'] = data['Yr'] + data['Mo'] + data['Dy'] + '0000'

data['Date'] = data['Date'].apply(lambda x: np.datetime64(x[:4] + '-'+x[4:6]+'-'+x[6:8]+' ' + x[8:10]+':'+x[10:], 'm'))

data.set_index('Date', inplace=True)


def to_float(x):
    try:
        x = float(x)
        if x > 50 or x < 0.0:
            x = 0.0
        return x
    except:
        x = 0.0
        return x


for column in data.columns[3:]:
    data[column] = data[column].apply(lambda x: to_float(x))
    data[column] = data[column].apply(lambda x: np.mean(data[column]) if x == 0.0 else x)

print(data.head())

# print(data.dtypes)

loc_stats = data.describe()

loc_stats.rename(index={'count':'count_of_NotNull'}, inplace=True)
for column in loc_stats.columns:
    loc_stats[column] = np.round(loc_stats[column], 3)
print(loc_stats)
null = len(data) - loc_stats.loc['count_of_NotNull']
print("Count_of_Null: \n", null)

january_mean_speed = data[data['Mo'] == '01'].mean()[3:]
print(january_mean_speed)

dict_locations = {column: 'mean' for column in data.columns[3:]}
year_mean_speed = data.groupby('Yr').agg(dict_locations)
print(year_mean_speed)

month_mean_speed = data.groupby('Mo').agg(dict_locations)
print(month_mean_speed)

#  2 января 1961 г.
x = '196101020000'
start_date = np.datetime64(x[:4] + '-'+x[4:6]+'-'+x[6:8]+' ' + x[8:10]+':'+x[10:], 'm')
data = data.loc[start_date:start_date + np.timedelta64(21 * 7 - 1, 'D')]

weeks = list(range(1, 22))
weeks_array = []
for week in weeks:
    for _ in range(7):
        weeks_array.append(week)

data['week'] = weeks_array

dict_locations = {column: ['min','max','mean', 'std'] for column in data.columns[3:len(data.columns)-1]}
data_weekly = data.groupby('week').agg(dict_locations)
print(data_weekly)
