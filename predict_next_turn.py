# get next turn
# calculate predict the next results
# Model
# T1 X T2
# T1 alpha, beta, gama (mandante, visitante)
# [alphax alphay betax betay gama]
def predict_next_turn(Mandante, Visitante):
    R1=Mandante.alpha*Visitante.beta;
    R2=Mandante.beta* Visitante.alpha;

    return R1, R2