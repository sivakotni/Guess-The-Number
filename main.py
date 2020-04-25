from random import randint
a=randint(0,1)
b=int(input('guess the number i have taken:'))
i=0
while(b!=a):
	if b>a:
		b=int(input('you are too high try another:'))
	else :
		b=int(input('you are too low try another:'))
	i+=1
print('you have won jackpot in {} tries'.format(i))
