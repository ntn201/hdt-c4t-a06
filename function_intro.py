def calculate_delta(a,b,c):
    return b*b - 4*a*c

def quadractic(a,b,c):
    # local variable
    # biến cục bộ
    # scope
    delta = calculate_delta(a,b,c)
    if delta < 0:
        return None
    if delta == 0:
        x = -b/2/a
        return x
    if delta > 0:
        x_1 = (-b+delta**0.5)/(2*a)
        x_2 = (-b-delta**0.5)/(2*a)
        return x_1, x_2

print(quadractic(1,-5,6))


def array_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum