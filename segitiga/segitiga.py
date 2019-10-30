p = float(input("Masukkan a : "))
q = float(input("Masukkan b : "))
r = float(input("Masukkan c : "))

def Segitiga(p,q,r):
	if (p<=0 or q<=0 or r<=0):
		hasil = "Segitiga tidak dapat dibangun"
	elif (p==q):
		hasil = "Segitiga Sama Kaki"
	elif (q==r):
		hasil = "Segitiga Sama Kaki"
	elif (p==r):
		hasil = "Segitiga Sama Kaki"
	elif (p == q == r):
		hasil = "Segitiga Sama Sisi"
	elif (p**2==q**2+r**2 or q**2==p**2+r**2 or r**2==q**2-p**2):
		hasil = "Segitiga Siku-Siku"
	else:
		hasil = "Segitiga Bebas"
	return hasil

print(Segitiga(p,q,r))
