# task3

import numpy as np


def lucky_series(num):
    series = np.random.choice([2, 3, 4, 5, 6, 7], num, p=[0.1, 0.1, 0.1, 0.3, 0.3, 0.1])
    print(series)

    series = np.where((series == 6) | (series == 5), series, 0)

    series_str = ''
    for num in series:
        series_str += str(num)

    series_dict = {i: len(i) for i in series_str.split('0') if i != '' and '6' in i and '5' in i}
    if len(series_dict) == 0:
        print("No lucky series( ")
        print(0)
    else:
        print("All lucky series: ")
        print(series_dict)
        max_lucky = max(series_dict.values())
        print("The longest length is: ", max_lucky)
        print("The Value of longest: ")
        for k in series_dict.keys():
            if series_dict[k] == max_lucky:
                print(k)


lucky_series(200)

# [5 7 2 5 7 3 4 6 2 7 5 3 6 3 5 6 6 2 5 5 3 7 6 6 6 5 7 6 4 3 2 3 5 5 5 5 6
#  6 5 6 7 2 5 5 6 7 5 6 6 5 3 6 6 6 2 2 5 7 6 7 4 6 6 7 4 2 6 6 6 4 5 5 6 6
#  7 4 6 7 5 3 6 6 7 5 7 4 2 6 2 2 5 5 4 6 5 5 5 6 6 5 7 2 7 6 7 2 5 5 2 2 7
#  5 4 6 6 5 2 6 5 5 6 5 5 5 6 5 7 6 7 5 5 2 3 5 5 5 5 6 7 6 5 6 2 7 5 6 5 3
#  6 5 5 7 6 5 7 4 7 6 5 5 6 5 4 4 5 6 6 5 2 6 5 6 6 3 4 4 2 6 6 6 5 4 4 6 3
#  5 4 3 6 7 3 2 6 6 2 2 4 4 4 3]
# All lucky series: 
# {'566': 3, '6665': 4, '55556656': 8, '556': 3, '5665': 4, '5566': 4, '6555665': 7, '665': 3, '655655565': 9, 
#  '55556': 5, '656': 3, '565': 3, '655': 3, '65': 2, '65565': 5, '6566': 4}
# The longest length is:  9
# The Value of longest: 
# 655655565
