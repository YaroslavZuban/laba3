import pandas as pd
import numpy
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Студент': ['Степан Белов', 'Сергей Даренко', 'Ира Белоглазова', 'Вика Марченко', 'Илья Горин'],
    'Курс': [2, 3, 1, 4, 2],
    'Факультет': ['РЭФ', 'РЭФ', 'ФЛА', 'ФМА', 'ФПМИ']
})

print(df, '\n')

df['Средняя балл'] = [3.5, 2.4, 4.6, 4.2, 5]
print(df, '\n')
pf = df

hl = df.groupby('Студент').agg('mean')
print(hl, '\n')

df = df.reset_index(drop=False)
print(df, '\n')

table = pd.pivot_table(pf, values='Средняя балл', index=['Факультет', 'Студент'], aggfunc=numpy.sum)
print(table, '\n')

# вывод графика виде точек

for index, i in enumerate(df['Средняя балл']):
    plt.plot(df.index[index], df.iloc[index]['Курс'], marker='.', linestyle='None', markersize=i * 4, color='b')
plt.show()
