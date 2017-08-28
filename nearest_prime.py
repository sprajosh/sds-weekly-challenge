def isprime(num):
    for x in xrange(2, int(num**0.5)+1):
        if num % x ==0:
            return False
    else:
        return True

def larger(num):
    found = False
    if num%2 == 0:
        num+=1
    while not found:
        if isprime(num):
            return num
        else:
            num+=2
            
def smaller(num):
    found = False
    if num%2 == 0:
        num-=1
    while not found and num > 2:
        if isprime(num):
            return num
        else:
            num-=2
    return 2

num = input()
print larger(num+1),  num, smaller(num-1)