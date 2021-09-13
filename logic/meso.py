import math

def meso(level, sf_now):
    if sf_now <= 9:
        meso_re = 1000 + pow(level,3) * (sf_now + 1) / 25

    elif sf_now <= 14:
        meso_re = 1000 + pow(level,3) * pow( (sf_now+1), 2.7) / 400

    else:
        meso_re = 1000 + pow(level,3) * (sf_now + 1) / 200

    return round(meso_re, 0)

