#ham kiem tra so nhi phan co chia het cho 5 hay khong
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2) #chuyen doi so nhi phan sang thap phan
    if so_thap_phan % 5 == 0: #kiem tra xem so thap phan co chia het cho 5 hay khong
        return True
    else:
        return False
#nhap chuoi so nhi phan tu nguoi dung
chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan(phan tach boi dau phay): ")
#tach chuoi so nhi phan thanh tung so va kiem tra tung so chia het cho 5 hay khong
so_nhi_phan_list = chuoi_so_nhi_phan.split(",")
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
#in ra cac so nhi phan chia het cho 5
if len(so_chia_het_cho_5)>0:
    ket_qua = ",".join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5.")