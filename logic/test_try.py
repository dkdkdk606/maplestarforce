from sf_once import starforce


level = int(input("몇렙장비?"))
equ_value = int(input("노작값 얼마?"))
star = int( input("몇성에서 시작?") )
star_try = int(input("몇번 시도?"))


meso_now = 0
fail = 0

for i in range(star_try):
    a = starforce(level, star, fail, meso_now, 10, 0, 0, equ_value)
    star = a[0]
    fail = a[1]
    meso_now = a[2]
    print(meso_now)
    if star == 25:
        print("와 미친", i, "번 강화해서 25강을 띄우네")
        break

print("총", meso_now, "메소 씀", "마무리는", star, "성")

