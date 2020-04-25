from random import randint
a=randint(0,1000)
b=int(input('guess the number i have taken:'))
while(b!=a):
	if b>a:
		b=int(input('you are too high try another:'))
	else :
		b=int(input('you are too low try another:'))
print('jackpot')
		



	


	
