# создали notebook
import pandas as pd
import numpy
import matplotlib.pyplot as plt
#1
df = pd.DataFrame({
    'Студент': ['Степан Белов', 'Сергей Даренко', 'Ира Белоглазова', 'Вика Марченко', 'Илья Горин'],
    'Курс': [2, 3, 1, 4, 2],
    'Факультет': ['РЭФ', 'РЭФ', 'ФЛА', 'ФМА', 'ФПМИ']
})

print(df, '\n')
#2
df['Средняя балл'] = [3.5, 2.4, 4.6, 4.2, 5]
print(df, '\n')
pf = df
#3
hl = df.groupby('Студент').agg('mean')
print(hl, '\n')

#6 загрузка таблицы с сайта
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data'
data = pd.read_csv(url, header=None, na_values='?')
print(data)

print("\n")

#5
df = df.reset_index(drop=False)
print(df, '\n')
#7
table = pd.pivot_table(pf, values='Средняя балл', index=['Факультет', 'Студент'], aggfunc=numpy.sum)
print(table, '\n')

#8 вывод графика виде точек

for index, i in enumerate(df['Средняя балл']):
    plt.plot(df.index[index], df.iloc[index]['Курс'], marker='.', linestyle='None', markersize=i * 4, color='b')
plt.show()
