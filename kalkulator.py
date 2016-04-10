def dodawanie(a, b):
	return a + b
try:	
	l1 = int(input())
	l2 = int(input())
	print(dodawanie(l1, l2))
except:
	print("Program zakoñczy³ sie nieoczekiwanym bledem")
	print("Mozesz go zglosic pod adresem pomoc@autor.pl")