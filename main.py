import pandas as pd
import math

df = pd.read_csv(
    'Tabela_de_Notas_PETUFES01_-_Introcomp.csv',
    sep=','
)
#df.info()

df = df.replace('-', 0)
df = df.drop(columns=['Nome Completo', 'Num. Matricula', 'Email', 'Tipo'])

sum = 0
rows_count = len(df.index) 
average_dic = {}

for column in df:
    for row in df[column]:
        sum += float(row)
    #print(f"Column: {column} average: {sum/rows_count}")
    average_dic[column] = sum/rows_count
    sum = 0

working_average = math.fsum(average_dic.values()) / len(average_dic)

print(f"Overall average of working: {working_average}")

print("==============================================")
print("Below average workings:")
print("==============================================")
for key, value in average_dic.items():
   
    if value <= working_average:
        print(f"Working: {key} average: {value}")