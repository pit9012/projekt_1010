def dodawanie(a, b):
	return a + b
	
def get_info():
	print("Program kalkulator. Autor: Piotr")

get_info()

try:	
	l1 = int(input())
	l2 = int(input())
	print(dodawanie(l1, l2))
except:
	print("Program zakoñczy³ sie nieoczekiwanym bledem")
	print("Mozesz go zglosic pod adresem pomoc@autor.pl")
	
