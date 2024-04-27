def round_up(num):
    number_rounded_up = int(num)
    if (num%1 != 0):
        number_rounded_up += 1
    return number_rounded_up

def before_half(num):
    half = num/2
    half_rounded_up = round_up(half)
    
    r = range(0, half_rounded_up)

    for i in r:
        print(num-i)

before_half(10)
        