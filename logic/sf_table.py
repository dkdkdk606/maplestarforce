import math

suc = [95, 90, 85, 85, 80, 75, 70, 65, 60, 55, 45, 35,
        30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 3, 2, 1]

fai = [5, 10, 15, 15, 20, 25, 30, 35, 40, 45, 55, 65,
        69.4, 68.7, 68.6, 67.9, 67.9, 67.9, 67.2, 67.2, 63.0, 63.0, 77.6, 68.6, 59.4]

sf_fai = [0.25, 5.5, 10.75, 10.75, 16.0, 21.25, 26.5, 31.75, 37.0, 42.25, 52.75, 63.25,
        67.91, 67.23, 67.13, 66.45, 66.45, 66.45, 65.76, 65.76, 61.65, 61.65, 77.48, 68.53, 59.37]

dis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.6, 1.3, 1.4, 2.1, 2.1, 2.1, 2.8, 2.8, 7.0, 7.0, 19.4, 29.4, 39.6]

sf_dis = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.59, 1.27, 1.37, 2.06, 2.06, 2.06, 2.74, 2.74, 6.85, 6.85, 19.37, 29.37, 39.58]

#검증용
#i = 0
#while i != 15:
#    print(sf_fai[i] + sf_dis[i] + suc[i]*1.05)
#    i += 1

#fail 그냥 위 처럼 숫자로 써넣는게 나을까?
#fail = []
#a = 0
#while a != len(suc):
#    fail.append(100 - suc[a] - dis[a])


# 그냥 숫자 넣는게 나을듯 해서 뺌
#    sf_fail = []
#    i = 0
#    while i != len(suc):
#        sf_fail.append( fai[i] - suc[i]*0.05 * fai[i]/(dis[i]+fai[i]) )
#        i += 1

def sf_succ(sf_now, starcatch):
    
    if starcatch == 1:
        return suc[sf_now] * 1.05
    else:
        return suc[sf_now]


def sf_fail(sf_now, starcatch):

    if starcatch == 1:
        return sf_fai[sf_now]
    else:
        return fai[sf_now]



def sf_dist(sf_now, starcatch):

    if starcatch == 1:
        return sf_dis[sf_now]
    else:
        return dis[sf_now]


def meso(level, sf_now):
    if sf_now <= 9:
        meso_re = 1000 + pow(level,3) * (sf_now + 1) / 25

    elif sf_now <= 14:
        meso_re = 1000 + pow(level,3) * pow( (sf_now+1), 2.7) / 400

    else:
        meso_re = 1000 + pow(level,3) * (sf_now + 1) / 200

    return round(meso_re, 0)



#a = 0
#while a != 25:
#    print(sf_suc(a), sf_dis(a), sf_fail(a))
#    a += 1


