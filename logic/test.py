from sf_once import starforce

meso_now = 0
star = int( input("몇성에서 시작?") )
fail = 0

try_1 = int(input("몇번 시도?"))

for i in range(try_1):
    a = starforce(200, star, fail, meso_now, 10, 0, 0)
    star = a[0]
    fail = a[1]
    meso_now = a[2]
    print(star)

print("총", meso_now, "메소 씀")
print("결과는", star, "성")

