from random import randint
a=randint(0,1000)
b=int(input('guess the number i have taken:'))
if b==a:
	print('jackpot')
while(b!=a):
	if b>a:
		b=int(input('you are too high try another:'))
		if b==a:
			print('jackpot')
	else :
		b=int(input('you are too low try another:'))
		if a==b:
			print('jackpot')
		



	


	
