import pandas as pd

df = pd.read_csv(
    'Tabela_de_Notas_PETUFES01_-_Introcomp.csv',
    sep=','
)
#df.info()

df = df.replace('-', 0)
df = df.drop(columns=['Nome Completo', 'Num. Matricula', 'Email', 'Tipo', 'M02W01E03', 'M02W01E04', 'M02W01E01', 'M02W01E02', 'M01W02O01', 'M01W02O02', 'M01W03O01', 'M01W05O02', 'M01W05O01', 'M01W04O01', 'M01W04O02', 'M01W02O03'])

# df.info()
col = df.shape[1]

df.iloc[1: , :]
for i in range(col):
    total = df[i].sum()
    print(total)
