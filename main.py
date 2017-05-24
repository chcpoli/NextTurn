import pandas as pd
from get_results import get_results
#from predict_next_turn import predict_next_turn
#from calc_stats import calc_stats

#Import Current Results
fileloc = 'D://Campeonato Brasileiro//resultados.txt'



db_CB = get_results(fileloc)
print(db_CB.head)

#Generate Statistics
#calc_stats()
#Predict Next Turn
#predict_next_turn()