# get_results(fileloc)
# Get last results from Campeonato Brasileiro and return the formated
# for each game: Mandante, Visistante, Gols Mandante, Gol Visitante, Dia desde início do Campeonato
# fileloc example:
# from get_results import get_results
# fileloc = \'D://Campeonato Brasileiro//resultados.txt\'
# db_CB=get_results(fileloc)
# and returns a pandas database as
# return df['Mandante','Visitante', 'gM', 'gV', 'day']
import pandas as pd

def get_results(fileloc = 'D://Campeonato Brasileiro//resultados.txt'):
    df = pd.read_csv(fileloc, header=None, delimiter='\t')
    df.columns = ['Data', 'Mandante', 'gMxgV', 'Visitante', 'CV', 'CE', 'CV']
    df['gM'], df['gV'] = df['gMxgV'].str.split('x', 1, expand=True).str
    df['dd'], df['mm'], df['aaaa'] = df['Data'].str.split('/', 2).str
    df['gM'] = df['gM'].astype('int64')
    df['gV'] = df['gV'].astype('int64')
    df['dd'] = df['dd'].astype('int64')
    df['mm'] = df['mm'].astype('int64')
    df['aaaa'] = df['aaaa'].astype('int64')
    df['day'] = df['dd'] + df['mm']*30
    df['day'] = df['day'] - df['day'].min()
    return df['Mandante','Visitante', 'gM', 'gV', 'day']