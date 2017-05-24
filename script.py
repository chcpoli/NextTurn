import pandas as pd

fileloc = 'D://Campeonato Brasileiro//resultados.txt'
df = pd.read_csv(fileloc, header=None, delimiter='\t')
df.columns = ['Data', 'Mandante', 'gMxgV', 'Visitante', 'CV', 'CE', 'CV']
df['gM'], df['gV'] = df['gMxgV'].str.split('x', 1).str
df['dd'], df['mm'], df['aaaa'] = df['Data'].str.split('/', 2).str
df['gM'] = df['gM'].astype('int64')
df['gV'] = df['gV'].astype('int64')
df['dd'] = df['dd'].astype('int64')
df['mm'] = df['mm'].astype('int64')
df['aaaa'] = df['aaaa'].astype('int64')
df['day'] = df['dd'] + df['mm']*30
df['day'] = df['day'] - df['day'].min()

df_CB = df[['Mandante','Visitante', 'gM', 'gV', 'day']]
