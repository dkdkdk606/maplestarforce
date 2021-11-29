from sf_once import starforce

level = int(input("몇렙장비?"))
equ_value = int(input("노작값 얼마?"))
star_ini = int( input("몇성에서 시작?") )
star_ter = int(input("몇성까지?"))
how_many = int(input("몇개 만듦?"))

meso_now = 0
meso_sum = 0
fail = 0
i = 0
j = 0

star = star_ini

for k in range(how_many):
    while i != -1:
        s = starforce(level, star, fail, meso_now, 0, 0, 0, 0, equ_value)
        star = s[0]
        fail = s[1]
        meso_now = s[2]
        i += 1

        if star == star_ter:
            print(i, "번", meso_now, "메소")
            meso_sum += meso_now
            j = j + i

            fail = 0
            meso_now = 0 
            i = 0
            star = star_ini

            break
    

print(level, "레벨 장비", star_ini, "→", star_ter,  how_many, "개 만들 때", "평균", j/how_many, "번", meso_sum/how_many, "메소 씀")
