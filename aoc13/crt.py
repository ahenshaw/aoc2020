from functools import reduce

def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

# print(t % 67 == 0)
# print(t % 7 == 6)
# print(t % 59 == 57)
# print(t % 61 == 58)

# n=[3,5,7]
# a=[2,3,2]
if __name__ == '__main__':
    n = [67, 7, 59, 61]
    a = [0, 6, 57, 58]
    print(chinese_remainder(n,a))