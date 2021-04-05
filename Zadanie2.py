#9
import time
import pandas as pd

start_time = time.time()
df = pd.DataFrame({
    'Регион': [24, 36, 8, 74, 56],
    'Курс': [2, 3, 1, 4, 2],
    'Факультет': [5, 9, 10, 14, 15]
})

pf = pd.DataFrame(df, columns=['Регион', 'Курс', 'Факультет'])
print(pf, '\n')

print("--- %s seconds ---" % (time.time() - start_time), '\n')

print(pf.corr(), '\n')