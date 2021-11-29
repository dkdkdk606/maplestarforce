import random

from sf_table import meso
from sf_table import sf_dist
from sf_process import sf_success
#from sf_process import sf_failure

def starforce(level, sf_now, fail, meso_now = 0, sale = 0, fifth = 0, starcatch = 0, dis_prevent = 0, equ_value = 0):
# 어 내가 하려는게 필요한 수치 넣으면 강화 한번 해주는거
# level 장비레벨,       sf_now 현스타포스 수치, (필요없네, sf_fin), fail찬스타임계산용,
# meso 현재까지 쓴 매소,    sale 할인 이벤트,       fifth 5,10,15 성공 이벤트
# dis_prevent 파방 함?,     equ_value 노작값
    if dis_prevent == 1 and sf_now in [12, 13, 14, 15, 16]:
        meso_now += meso(level, sf_now) * (1-0.01*sale) * 2
    
    else:
        meso_now += meso(level, sf_now) * (1-0.01*sale)

#세일, fifth 정의 필요
#lucky는 낮을수록 좋은 느낌으로 높으면 실패 더높으면 파괴
    lucky = random.uniform(0, 100)

# 성공은 여러가지 경우 이벤트, 2연속 실패 등 이 있어서 프로세스에 결과값까지 나올수 있게 함

    if lucky <= sf_success(sf_now, fail, fifth, starcatch):
        sf_now += 1
        fail = 0

    
# 성공할만큼 운좋진 않고 파괴될만큼 운 안좋진 않다면
    elif lucky <= 100 - sf_dist(sf_now, starcatch) or (dis_prevent == 1 and sf_now in [12, 13, 14, 15, 16]):


#        sf_failure(sf_now, fail) #함수 안에서 sf_now가 하나 낮아져서 나와야하는데 지역함수 취급이어서 안나오네 즉 밖에 빼야하네 ㅄ
        if sf_now not in [0, 1, 2, 3, 4, 5, 10, 15, 20]: #각 강화에선 유지니까 내릴필요 없 
            fail += 1
            sf_now -= 1

    else:           #성공도 아니고 실패도 아니니 파괴
        fail = 0
        sf_now = 12
        meso_now += equ_value

    
    return [sf_now, fail, meso_now]

          # 성공도 실패도 아니다? 바로 파괴
          # 10까지는 안떨구고 파괴 이런것도 다 넣음 실패확률 0 으로 파괴는 ㄴㄴ
    

#for i in range(22):
#    print(i, meso(200,i))