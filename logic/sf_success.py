from table import sf_suc


def sf_success(sf_now, fail, fifth, starcatch):
    if fail == 2:
        fail = 0
        return 100
    
    elif fifth == 1 and sf_now in [5,10,15]:
        return 100

    elif starcatch == 1:
        return sf_suc(sf_now) * 1.05

    else:
        return sf_suc(sf_now)
    
    
    