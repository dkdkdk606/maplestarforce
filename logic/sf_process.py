from sf_table import sf_succ


def sf_success(sf_now, fail, fifth, starcatch):
    if fail == 2:
        fail = 0
        return 100.0
    
    elif fifth == 1 and sf_now in [5,10,15]:
        return 100.0

    else:
        return sf_succ(sf_now, starcatch)
    
def sf_failure(sf_now, fail):

    if sf_now not in [0, 1, 2, 3, 4, 5, 10, 15, 20]:
        fail += 1
        sf_now -= 1
    return
#왜 fail 참조가 안될까??????????????????????? 엄란어라ㅣㅁㄴ어라ㅓ나ㅣㅏ
    