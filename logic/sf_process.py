from sf_table import sf_succ


def sf_success(sf_now, fail, fifth, starcatch):
    if fail == 2:
        #fail = 0  함수 안에서 전역변수 못바꾼다!

        return 100.0
    
    elif fifth == 1 and sf_now in [5,10,15]:

        return 100.0

    else:

        return sf_succ(sf_now, starcatch)
    
#def sf_failure(sf_now, fail): 
#    if sf_now not in [0, 1, 2, 3, 4, 5, 10, 15, 20]:       
#        fail += 1
#        sf_now -= 1
#    reuturn
        #이런거 넣으면 안되네 밖에다가 빼서 해야지 하는방법 있긴 할라나
        #필요는 없지만 일단 남겨놓음



#왜 fail 참조가 안될까??????????????????????? 엄란어라ㅣㅁㄴ어라ㅓ나ㅣㅏ
    