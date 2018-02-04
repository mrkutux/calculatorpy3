#tambah
def tambah (a,b):
	return a+b

#kurang
def kurang (a,b):
	return a-b

#bagi
def bagi (a,b):
	return a/b

#kali
def kali (a,b):
	return a*b

#Menu
print("|==========================|")
print("|=Kalkulator By Helmy Agta=|")
print("|==========================|")
print("|========Pilih Menu========|")
print("|===< 1. Penjumlahan >=====|")
print("|===< 2. Pengurangan >=====|")
print("|===< 3. Pembagian   >=====|")
print("|===< 4. Perkalian   >=====|")
print("|==========================|")

#InputUser
choice = input("Masukan Pilihan (1/2/3/4):")

angka1 = int(input("Masukan Bilangan Pertama :"))
angka2 = int(input("Masukan Bilangan Kedua :"))

if choice == '1':
	print(angka1,"+",angka2,"=",tambah(angka1,angka2))
elif choice == '2':
	print(angka1,"-",angka2,"=",kurang(angka1,angka2))
elif choice == '3':
	print(angka1,":",angka2,"=",bagi(angka1,angka2))
elif choice == '4':
	print(angka1,"x",angka2,"=",kali(angka1,angka2))
else:
	print("Ngetik yg bner ya :)")