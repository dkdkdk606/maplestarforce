import math


def sf_suc(sf_now, starcatch):
    suc = [95 - 5 * sf_now, 95 - 5 * sf_now, 95 - 5 * sf_now,
            95 - 5 * sf_now, 95 - 5 * sf_now, 95 - 5 * sf_now,
            95 - 5 * sf_now, 95 - 5 * sf_now, 95 - 5 * sf_now,
            100 - 5 * sf_now, 100 - 5 * sf_now, 100 - 5 * sf_now,
             100 - 5 * sf_now, 100 - 5 * sf_now, 100 - 5 * sf_now,
             30, 30, 30, 30, 30, 30, 30, 3, 2, 1]

    return suc[sf_now]

def sf_dis(sf_now, starcatch):
    dis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0.6, 1.3, 1.4, 2.1, 2.1, 2.1, 2.8, 2.8, 7.0, 7.0, 19.4, 29.4, 39.6]
    return dis[sf_now]


def sf_fail(sf_now, starcatch):
    return 100 - sf_suc(sf_now) - sf_dis(sf_now)


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

