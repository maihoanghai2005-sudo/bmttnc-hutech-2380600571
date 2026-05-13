so_gio_lam = float(input("Nhap so gio lam: "))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan "))
gio_tieu_chuan = 44 #so gio lam tieu chuan trong 1 tuan
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan) #tinh so gio lam vuot chuan
thuc_linh = (gio_tieu_chuan * luong_gio) + (gio_vuot_chuan * luong_gio * 1.5) #tinh thuc linh
print(f"Thuc linh cua nhan vien: {thuc_linh}")