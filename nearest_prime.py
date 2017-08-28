def isprime(num):
    prime = True
    for y in xrange(2, int(num**0.5)+1):
        if num % y ==0:
            return False
    else:
        return True

def larger(num):
    found = False
    if num%2 == 0:
        num+=1
    while not found:
        if isprime(num):
            found = True
        else:
            num+=2
    return num
            
def smaller(num):
    found = False
    if num%2 == 0:
        num-=1
    while not found and num > 0:
        if isprime(num):
            found = True
        else:
            num-=2
    return num


num = input()
print larger(num+1),  num, smaller(num-1)
