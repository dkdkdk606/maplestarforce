import random

from sf_fail import sf_fail
from sf_fail import sf_dis
from meso import meso
import sf_success

def starforce(level, sf_now, fail, meso_now, sale, fifth):

# 어 내가 하려는게 필요한 수치 넣으면 강화 한번 해주는거
# level 장비레벨,       sf_now 현스타포스 수치, (필요없네, sf_fin), fail찬스타임계산용,
# meso 현재 쓴 매소,    sale 할인 이벤트,       fifth 5,10,15 성공 이벤트
    meso_now = meso_now + meso(level, sf_now) * sale
#세일, fifth 정의 필요
    lucky = random.uniform(0, 100)
    if lucky <= sf_success(level, sf_now, fail, fifth):
        sf_now += 1

    elif lucky > 100 - sf_dis(sf_now):
        fail = 0
        sf_now = 12

    else:
        sf_now = sf_fail(level, sf_now, fail)
        # 10까지는 안떨구고 파괴 이런것도 다 넣어야하나 파괴는 ㄴㄴ
    
    
    


