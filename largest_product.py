def prod(num):
    '''accepts a string and returns product of all digits in the string'''
    product = 1
    for x in num:
        product *= int(x)
    return product

num = input("Enter the number: ")
k = int(input("Number of digits: "))
end, start, maxx = 0, 0, 0
while len(num[start:k]) == k-start:
    p = prod(num[start:k])
    if maxx < p:    maxx = p
    start, k = start+1, k+1
print(maxx)
