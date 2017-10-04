__author__ = 'batefirok'

def sum_of_multiples():
    #init sum to zero
    sum =0
    for i in range(1000):
        if i%3==0 or i%5==0:
            sum+=i
    return sum

print(sum_of_multiples())