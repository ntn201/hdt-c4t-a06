cot_1 = [1,2,3,4,5]
cot_2 = []
cot_3 = []
                
# cot_3.insert(0,cot_1.pop(0))


def move(n,cot_xp,cot_tg,cot_dich):
    if n == 1:
        cot_dich.insert(0,cot_xp.pop(0))
    else:
        move(n-1,cot_xp,cot_dich,cot_tg)
        cot_dich.insert(0,cot_xp.pop(0))
        move(n-1,cot_tg,cot_xp,cot_dich)
move(5,cot_1,cot_2,cot_3)
print(cot_1,cot_2,cot_3)
    # chuyen n-1 vong tu xp -> tg
    # chuyen vong thu n tu xp -> dich
    # chuyen n-1 vong tu tg -> dich



