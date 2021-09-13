def sf_fail(level, sf_now, fail):
    if sf_now > 10:
        fail += 1
        sf_now -= 1

def sf_dis(sf_now):
    dis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 1.3, 1.4, 2.1, 2.1, 2.1, 2.8, 2.8, 7.0, 7.0, 19.4, 29.4, 39.6]
    
    return dis[sf_now]

print(sf_dis(3))