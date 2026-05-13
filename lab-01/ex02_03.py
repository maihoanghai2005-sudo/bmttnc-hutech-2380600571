#nhap so nguoi dung
so = int(input("Nhap so nguyen: "))
#kiem tra so do co phai la so chan hay khong
if so % 2 == 0:
    print(so, "la so chan") 
else:
    print(so, "la so le")