import random

def addition(x,y):
    z = x + y
    return z

def subtraction(x,y):
    z = x - y
    return z

konnichiha = 'こんにちは'
print(konnichiha)

x = 1
y = 2
print(str(x) + '+' + str(y) + '=' + str(addition(x,y)))
print(str(x) + '-' + str(y) + '=' + str(subtraction(x,y)))

n = random.randrange(-10,10)
print(n)
if n < 0 :
    print('nは負の数です')
elif n > 0 :
    print('nは正の数です')
else :
    print('nは0です')

numList = []
for i in range(10,20) :
    numList.append(i)

for num in numList :
    print(num)

