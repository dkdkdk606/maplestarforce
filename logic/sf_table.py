import math

suc = [95.0, 90.0, 85.0, 85.0, 80.0, 75.0, 70.0, 65.0, 60.0, 55.0, 50.0, 45.0,
            40.0, 35.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 3.0, 2.0, 1.0]

sf_suc = [99.75, 94.5, 89.25, 89.25, 84.0, 78.75, 73.5, 68.25, 63.0, 57.75, 52.50, 47.25,
            42.0, 36.75, 31.50, 31.5, 31.5, 31.5, 31.5, 31.5, 31.5, 31.5, 3.15, 2.1, 1.05]

fai = [5.0, 10.0, 15.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0,
            59.4, 63.7, 68.6, 67.9, 67.9, 67.9, 67.2, 67.2, 63.0, 63.0, 77.6, 68.6, 59.0]

sf_fai = [0.25, 5.5, 10.75, 10.75, 16.0, 21.25, 26.5, 31.75, 37.0, 42.25, 47.50, 52.75,
            57.42, 61.99, 67.13, 66.45, 66.45, 66.45, 65.76, 65.76, 61.65, 61.65, 77.48, 68.53, 59.37]

dis = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.6, 1.3, 1.4, 2.1, 2.1, 2.1, 2.8, 2.8, 7.0, 7.0, 19.4, 29.4, 40]

sf_dis = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.58, 1.27, 1.37, 2.06, 2.06, 2.06, 2.74, 2.74, 6.85, 6.85, 19.37, 29.37, 39.58]

#print(42+57.42+0.58, 36.75+61.99+1.26, 31.5+67.13+1.37)


#검증용 이걸로 안하고 표에있는거 직접 쓰고 성공도 파괴도 아닌 확률은  실패로
#i = 0
#while i != 25:
#    print(i+1, sf_fai[i] + sf_dis[i] + sf_suc[i])
#    print(i+1, fai[i] + dis[i] + suc[i])
#    i += 1

#print(len(suc), len(fai), len(sf_dis), len(sf_fai), len(dis))

#fail 그냥 위 처럼 숫자로 써넣는게 나을까?
#fail = []
#a = 0
#while a != len(suc):
#    fail.append(100 - suc[a] - dis[a])


# 그냥 숫자 넣는게 나을듯 해서 뺌
#sf_fail = []
#i = 0
#while i != 25:
#    sf_fail.append(round(100 - sf_suc[i] - sf_dis[i], 2))
#    i += 1   
#print(sf_fail)
#   sf_fail.append( round(fai[i] - suc[i]*0.05 * fai[i]/(dis[i]+fai[i])))
#   버려진 식
def sf_succ(sf_now, starcatch):
    
    if starcatch == 1:
        return sf_suc[sf_now]
    else:
        return suc[sf_now]



#def sf_fail(sf_now, starcatch):
#
#    if starcatch == 1:
#        return sf_fai[sf_now]
#    else:
#        return fai[sf_now]



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
        meso_re = 1000 + pow(level,3) * pow( (sf_now+1), 2.7) / 200

    return round(meso_re, 0)



#a = 0
#while a != 25:
#    print(sf_suc(a), sf_dis(a), sf_fail(a))
#    a += 1

#for i in range(22):
#    print(i, meso(200,i))
