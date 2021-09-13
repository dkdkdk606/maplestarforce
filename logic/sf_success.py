baack = 100
def sf_suc_p(level, sf_now):
    if sf_now <= 9:
        p = 95 - 5 * sf_now
    elif sf_now <= 14:
        p = 100 - 5 * sf_now
    elif sf_now <= 21:
        p = 30
    elif sf_now == 22:
        p = 3
    elif sf_now == 23:
        p = 2
    else:
        p = 1

    return p

def sf_success(level, sf_now, fail, fifth):
    if fail == 2:
        fail = 0
        return baack
    
    elif fifth == 1 and sf_now in [5,10,15]:
        return baack

    else:
        return sf_suc_p(level, sf_now)
    
    
    